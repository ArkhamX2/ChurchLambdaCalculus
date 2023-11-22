import sys
import unittest
# setting path
sys.path.append('../library/')

from library.logical_parser import *

class Test(unittest.TestCase):
    def init():
        unittest.main()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isOperator(self):
        self.assertEqual(isOperator("¬"),True)        

    def test_Priority(self):
        self.assertEqual(Priority("¬"),4)

    def test_Parse(self):
        self.assertEqual(LogicalParse("¬ True ∧ True"),['True', '¬', 'True', '∧'])
