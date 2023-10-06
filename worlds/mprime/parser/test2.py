from ast import BoolOp, And
from timeit import timeit

def manual():
  BoolOp(And(), [BoolOp(And(), [BoolOp(And(), [BoolOp(And(), [BoolOp(And(), [])])])])])
    
def b(children = None):
  a = BoolOp(And(), [children])

def using_def():
  a = b(b(b(b(b()))))
    
TIMES = 1000000

times = sorted([
  (func.__name__, timeit(func, number=TIMES) / TIMES) for func in (
    manual,
    using_def
  )
], key=lambda x: x[1])

for funcname, time in times:
  print(f"{funcname}: {time * 1_000_000:.3f}us")