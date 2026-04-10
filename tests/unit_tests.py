import unittest
import pycalc.pycalc as calculator

class PyCalcUnitTests(unittest.TestCase):
  def test_add(self):
    left = [12, 44, 7, 1, 54, 0, 0, 0, -12, -44, -7, -1, -54]
    right = [48, 0, -3, -1, -102, 6, 0, -6, 20, 44, 2, 0, -12]
    expected = [60, 44, 4, 0, -48, 6, 0, -6, 8, 0, -5, -1, -66]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.add(l, r)
        self.assertEqual(got, e)
  def test_subtract(self):
    left = [12, 44, 7, 1, 54, 0, 0, 0, -12, -44, -7, -1, -54]
    right = [2, 44, 17, 0, -22, 23, 0, -5, 45, 0, -10, -1, -22]
    expected = [10, 0, -10, 1, 76, -23, 0, 5, -57, -44, 3, 0, -32]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.subtract(l, r)
        self.assertEqual(got, e)
  def test_multiply(self):
    left = [3, 5, 10, 0, 0, 0, -3, -5, -10]
    right = [4, 0, -4, 7, 0, -7, 3, 0, -3]
    expected = [12, 0, -40, 0, 0, 0, -9, 0, 30]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.multiply(l, r)
        self.assertEqual(got, e)

if __name__ == '__main__':
  unittest.main()
