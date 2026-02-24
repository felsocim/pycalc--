import sys
import pycalc.pycalc as calculator

def parse():
  if len(sys.argv) != 4:
    raise ValueError('Failed to parse command line')
  else:
    left = float(sys.argv[1])
    operation = sys.argv[2]
    right = float(sys.argv[3])
    return left, operation, right

try:
  left, operation, right = parse()
except ValueError:
  print('Invalid arithmetic expression!', file=sys.stderr)
  sys.exit(1)

result = None

if operation == '+':
  result = calculator.add(left, right)
elif operation == '-':
  result = calculator.subtract(left, right)
elif operation == '*':
  result = calculator.multiply(left, right)
elif operation == '/':
  result = calculator.divide(left, right)
else:
  print('Unknown operator!', file=sys.stderr)
  sys.exit(1)

print(result)
