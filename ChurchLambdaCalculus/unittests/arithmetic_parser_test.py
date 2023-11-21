import sys
import unittest
# setting path
sys.path.append('../library/')

from library.arithmetic_parser import *

class Test(unittest.TestCase):
    def init():
        unittest.main()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isOperator(self):
        self.assertEqual(isOperator("-"),True)        

    def test_Priority(self):
        self.assertEqual(Priority("*"),2)

    def test_Parse(self):
        self.assertEqual(ArithmeticParse("5 + ( 6 + 10 + 3 * ( 22 + 65 ) + 16 ) + 2 + 1"),['5', '6', '10', '+', '3', '22', '65', '+', '*', '+', '16', '+', '+', '2', '+', '1', '+'])
