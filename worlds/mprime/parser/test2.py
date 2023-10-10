from timeit import timeit

# def manual():
#   BoolOp(And(), [BoolOp(And(), [BoolOp(And(), [BoolOp(And(), [BoolOp(And(), [])])])])])
#     
# def b(children = None):
#   a = BoolOp(And(), [children])
# 
# def using_def():
#   a = b(b(b(b(b()))))

d = {}
for i in range(1000):
  d[str(i)] = 0

def with_dict():
  for i in range(1000):
    a = d.__getitem__(str(i))

obj_t = type('obj', (), {str(i): 0 for i in range(1000)})
obj = obj_t()

def with_attrs():
  for i in range(1000):
    a = getattr(obj, str(i))

    
TIMES = 1000

times = sorted([
  (func.__name__, timeit(func, number=TIMES) / TIMES) for func in (
    with_attrs,
    with_dict
  )
], key=lambda x: x[1])

for funcname, time in times:
  print(f"{funcname}: {time * 1_000_000:.3f}us")