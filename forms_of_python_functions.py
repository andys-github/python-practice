def non_default_args(a, b):
  print("Non-default Parameters: ", a, b)

def default_args(a, b, c = 100):
  print("Non-default Parameters: ", a, b)
  print("Default Parameters: ", c)

def with_non_kwargs(a, b, *args):
  print("Non-default Parameters: ", a, b)
  print("Non-keyword Arguments: ", args)

def with_kwargs(a, b, **kwargs):
  print("Non-default Parameters: ", a, b)
  print("Keyword Arguments: ", kwargs)

def with_both_kw_and_nonkw_args(a, b, *args, **kwargs):
  print("Non-default Parameters: ", a, b)
  print("Non-keyword Arguments: ", args)
  print("Keyword Arguments: ", kwargs)

non_default_args(10, 20)
print("------")
default_args(10, 20)
print("------")
with_non_kwargs(10, 20, 1, 2, 3, 4, 5)
print("------")
with_kwargs(10, 20, x = 1, y = 2, z = 3)
print("------")
with_both_kw_and_nonkw_args(10, 20, 1, 2, 3, x = 100, y = 200)
print("------")
