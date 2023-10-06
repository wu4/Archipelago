from timeit import timeit

obj = {}

def setup():
  obj = {}

def naive_obj_set():
  for n in range(10000):
    obj[f"Key{n}"] = n
    
def naive_setdefault():
  for n in range(10000):
    obj.setdefault(f"Key{n}", n)
    
def setdefault():
  f = obj.setdefault
  for n in range(10000):
    f(f"Key{n}", n)

def comprehension():
  obj = {
    f"Key{n}" for n in range(10000)
  }

from typing import Any
import ast
using_ast_and_exec_compiled: Any
def using_ast_and_exec_setup():
  global using_ast_and_exec_compiled
  using_ast_and_exec_compiled = compile(ast.parse("global obj; obj = {" + ",".join(f"'Key{n}': {n}" for n in range(10000)) + "}"), "<inline>", "exec")

def using_ast_and_exec():
  global obj
  exec(using_ast_and_exec_compiled, {'obj': obj})

using_ast_and_lambda_compiled: Any
def using_ast_and_lambda_setup():
  global using_ast_and_lambda_compiled
  using_ast_and_lambda_compiled = eval(compile(ast.Expression(ast.parse("lambda: {" + ",".join(f"'Key{n}': {n}" for n in range(10000)) + "}").body[0].value), "<inline>", "eval"))

def using_ast_and_lambda():
  global obj
  obj = using_ast_and_lambda_compiled()
TOTAL_REPS = 1000

from typing import Callable
def get_time_for(func: Callable, setupfunc: Callable = setup) -> tuple[str, float]:
  return (func.__name__, timeit(func, setupfunc, number = TOTAL_REPS, globals={"obj": {}}) / TOTAL_REPS)

times = sorted(list(map(lambda x: get_time_for(x[0], x[1]) if len(x) == 2 else get_time_for(x[0]), (
  (using_ast_and_exec,using_ast_and_exec_setup),
  (using_ast_and_lambda,using_ast_and_lambda_setup),
  (naive_obj_set,),
  (naive_setdefault,),
  (setdefault,),
  (comprehension,),
))), key=lambda x: x[1])

# print(obj)

for name, time in times:
  print(f"{name}: {(time * 1000):.4f}ms")
