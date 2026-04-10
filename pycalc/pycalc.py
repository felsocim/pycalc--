def add(a, b):
  res = a
  if b > 0:
    while (b - 1) >= 0:
      b -= 1
      res += 1
  elif b < 0:
    while (b + 1) <= 0:
      b += 1
      res -= 1
  return res

def subtract(a, b):
  res = 0
  if b < a:
    while b < a:
      b += 1
      res += 1
  elif b > a:
    while b > a:
      b -= 1
      res -= 1
  return res

def multiply(a, b):
  pass
def divide(a, b):
  pass
