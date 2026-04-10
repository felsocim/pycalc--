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
  if a == 0 or b == 0:
    return 0
  res = 0
  tmp_a = a if a > 0 else -a
  tmp_b = b if b > 0 else -b
  while tmp_b > 0:
    res += tmp_a
    tmp_b -= 1
  res = -res if (a < 0) ^ (b < 0) else res
  return res

def divide(a, b):
  if b == 0:
    raise ZeroDivisionError
  if a == 0:
    return 0
  res = 0
  tmp_a = a if a > 0 else -a
  tmp_b = b if b > 0 else -b
  while (tmp_a - tmp_b) >= 0:
    tmp_a -= tmp_b
    res += 1
  res = -res if (a < 0) ^ (b < 0) else res
  return res
