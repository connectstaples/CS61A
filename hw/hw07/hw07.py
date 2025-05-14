def pow(base, exp):
  """
  Calculates base raised to the power of exp using recursion,
  with the number of recursive calls growing logarithmically with respect to exp.
  """
  if exp == 0:
    return 1
  if exp == 1:
    return base
  if exp % 2 == 0:  # even
    return pow(base * base, exp // 2)  # Square the base and halve the exponent
  else:             # odd
    return base * pow(base * base, (exp - 1) // 2)  # Square the base, halve the exponent, and multiply by base

def repeat_cube(x, n):
  if n == 0:
    return x
  else:
    # (((x * n) * n) * n) # this computes but does not return 
    return repeat_cube(x**3, (n-1))  # return repeat_cube(x * x * x, n - 1) is also valid


  
  