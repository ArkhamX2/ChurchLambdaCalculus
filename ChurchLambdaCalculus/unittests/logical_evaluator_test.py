import sys
import unittest
# setting path
sys.path.append('../library/')

from library.logical_evaluator import *
from library.function import *

class Test(unittest.TestCase):
    def init():
        unittest.main()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_EvaluateEquation(self):
        self.assertEqual(eval(EvaluateLogicalEquation(['True', '¬', 'True', '∧'])),False)