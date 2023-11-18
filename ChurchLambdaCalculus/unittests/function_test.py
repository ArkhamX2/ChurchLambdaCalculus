import sys
import unittest
# setting path
sys.path.append('../library/')

from library.function import *

class Test(unittest.TestCase):
    def init():
        unittest.main()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_TRUE(self):
        self.assertEqual(TRUE,TRUE)

    def test_FALSE(self):
        self.assertEqual(FALSE,FALSE)

    def test_NOT(self):
        self.assertEqual(NOT(TRUE),FALSE)

    def test_OR(self):
        self.assertEqual(OR(FALSE)(TRUE),TRUE)

    def test_AND(self):
        self.assertEqual(AND(TRUE)(FALSE),FALSE)

    def test_XOR(self):
        self.assertEqual(XOR(TRUE)(FALSE),TRUE)

    def test_XNOR(self):
        self.assertEqual(XNOR(TRUE)(FALSE),FALSE)

    def test_ADD(self):
        self.assertEqual(encodeNatural(ADD(decodeNatural(4))(decodeNatural(7))),11)

    def test_MULTIPLY(self):
        self.assertEqual(encodeNatural(MULTIPLY(decodeNatural(4))(decodeNatural(7))),28)

    def test_SUBTRACT(self):
        self.assertEqual(encodeNatural(SUBTRACT(decodeNatural(10))(decodeNatural(7))),3)

    def test_POWER(self):
        self.assertEqual(encodeNatural(POWER(decodeNatural(10))(decodeNatural(7))),10000000)

    def test_DIFF(self):
        self.assertEqual(encodeNatural(DIFF(decodeNatural(14))(decodeNatural(7))),7)

    def test_DIVIDE(self):
        self.assertEqual(encodeNatural(DIVIDE(decodeNatural(14))(decodeNatural(7))),2)
