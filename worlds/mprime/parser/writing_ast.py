from typing import Iterable

implemented: set[str] = set()

def implements(*funcnames: str):
  for f in funcnames:
    implemented.add(f)
  def inner(func):
    return func
  return inner

def as_list(*args: str) -> str:
  return f"[{','.join(args)}]"

def quoted_str(string: str) -> str:
  return f"'{string}'"

def fill_lineno(funcname: str, *args: str) -> str:
  return f"{funcname}({','.join(args)},lineno=0,col_offset=0,end_lineno=0,end_col_offset=0)"


shortened_names: dict[str, str] = {
  "And": "A",
  "Attribute": "a",
  "arguments": "R",
  "arg": "r",
  "BoolOp": "B",
  "Call": "C",
  "Constant": "c",
  "Compare": "M",
  "GtE": "g",
  "Lambda": "L",
  "Load": "x",
  "Name": "N",
  "Not": "X",
  "Or": "O",
  "UnaryOp": "U"
}

import_str = f"from ast import {','.join(f'{k} as {v}' for k, v in shortened_names.items())}"

ENSURE_NO_COLLISIONS = True
if ENSURE_NO_COLLISIONS:
  occupied_letters = [
    'o', # options
    'l', # logic
    'p', # player
  ]

  cache = set()
  for val in shortened_names.values():
    if val in cache or val in occupied_letters:
      colliding_values = [(k, v) for k, v in shortened_names.items() if v == val]
      raise IndexError(f"shortened names collision: {colliding_values}")
    cache.add(val)

def short(n: str) -> str:
  return shortened_names[n]

@implements("BoolOp", "And")
def And(*children: str) -> str:
  return fill_lineno(short("BoolOp"), short('And') + "()", as_list(*children))

@implements("BoolOp", "Or")
def Or(*children: str) -> str:
  return fill_lineno(short("BoolOp"), short('Or') + "()", as_list(*children))

@implements("UnaryOp", "Not")
def Not(child: str) -> str:
  return fill_lineno(short("UnaryOp"), short('Not') + "()", child)

@implements("Constant")
def Constant(c: str) -> str:
  return fill_lineno(short("Constant"), c)

@implements("Name")
def Name(name: str) -> str:
  return fill_lineno(short("Name"), quoted_str(name), short("Load") + "()")

def LogicCall(funcname: str, *args: str) -> str:
  """
  Result:
  ```
  logic.<funcname>(state, player, *args)
  ```"""
  return Call(
    fill_lineno(short("Attribute"), Name('l'), quoted_str(funcname), short("Load") + "()"),
    Name('s'),
    Constant('p'),
    *args
  )
  
def StateHas(itemname: str) -> str:
  return Call(
    fill_lineno(short("Attribute"), Name("s"), quoted_str("has"), short("Load") + "()"),
    Constant(quoted_str(itemname)),
    Constant('p')
  )

def StateCountGtE(itemname: str, amount: int) -> str:
  return GtE(
    Call(
      fill_lineno(short("Attribute"), Name("s"), quoted_str("count"), short("Load") + "()"),
      Constant(quoted_str(itemname)),
      Constant('p')
    ),
    Constant(str(amount)),
  )

@implements("Compare", "GtE")
def GtE(lh: str, rh: str) -> str:
  return fill_lineno(short("Compare"), lh, as_list(short("GtE") + "()"), as_list(rh))

@implements("arguments")
def arguments(*argnames: str) -> str:
  return fill_lineno(short("arguments"), "[]", as_list(*map(lambda n: fill_lineno(short("arg"), quoted_str(n)), argnames)), "kwonlyargs=[]", "kw_defaults=[]", "defaults=[]")
  
@implements("Lambda")
def Lambda(argnames: Iterable[str], body: str) -> str:
  return fill_lineno(short("Lambda"), arguments(*argnames), body)

@implements("Call")
def Call(func: str, *args: str) -> str:
  return fill_lineno(short("Call"), func, as_list(*args), "[]")

if False:
  import ast
  import inspect
  gs = globals().copy()

  def needs_lineno(cls) -> bool:
    cls = cls[1]
    for p in ['expr', 'mod']:
      p_cls = getattr(ast, p)
      if cls == p_cls:
        return False
      elif issubclass(cls, p_cls):
        return True
    return False

  def only_class_attrs(namespace):
    clss = []
    for name in dir(namespace):
      cls = getattr(namespace, name)
      if not inspect.isclass(cls): continue
      clss.append((name, cls))
    return clss

  for name, cls in filter(needs_lineno, only_class_attrs(ast)):
    if name in implemented: continue
    print(name)