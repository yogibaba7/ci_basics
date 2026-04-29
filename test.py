
# test_app.py

import unittest
from app import sum, sub, mul

class TestMathFunctions(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(4, 5), 9)
        self.assertEqual(sum(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(4, 5), -1)
        self.assertEqual(sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()