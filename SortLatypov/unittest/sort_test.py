import sys

sys.path.append("../")

import unittest
from main import QuickSort


class MyTestCase(unittest.TestCase):

    def init():
        unittest.main()

    def test_Sort1(self):
        self.assertEqual(12,1)

    def test_Sort2(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()