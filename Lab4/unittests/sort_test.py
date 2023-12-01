import sys

sys.path.append('../library/')

import unittest
from library.sort import QuickSort

class MyTestCase(unittest.TestCase):

    def init():
        unittest.main()

    def test_Sort1(self):
        self.assertEqual(QuickSort([3,1,5]),[1,3,5])

    def test_Sort2(self):
        self.assertEqual(QuickSort([3,1,55,6,12,5,10,42,11]),[1,3,5,6,10,11,12,42,55])
