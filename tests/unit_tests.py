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

if __name__ == '__main__':
  unittest.main()
