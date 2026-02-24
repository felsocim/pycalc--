import unittest
from pycalc.pycalc import PyCalc

class PyCalcUnitTests(unittest.TestCase):
  def setUp(self):
    self.pycalc = PyCalc()
  def test_add(self):
    left = [5]
    right = [9]
    expected = [14]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = self.pycalc.add(l, r)
        self.assertEqual(got, e)

if __name__ == '__main__':
  unittest.main()
