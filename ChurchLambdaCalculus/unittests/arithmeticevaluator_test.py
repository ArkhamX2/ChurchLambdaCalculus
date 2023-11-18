import sys
import unittest
# setting path
sys.path.append('../library/')

from library.arithmeticevaluator import *
from library.function import *

class Test(unittest.TestCase):
    def init():
        unittest.main()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_EvaluateEquation(self):
        self.assertEqual(eval(EvaluateEquation(['5', '6', '10', '+', '3', '22', '65', '+', '*', '+', '16', '+', '+', '2', '+', '1', '+'])),301)