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

    def test_IS_ZERO(self):
        self.assertEqual(IS_ZERO(decodeNatural(0)),TRUE)
    
    def test_IS_GREATER_OR_EQUAL(self):
        self.assertEqual(IS_GREATER_OR_EQUAL(decodeNatural(2))(decodeNatural(4)),FALSE)

    def test_IS_GREATER(self):
        self.assertEqual(IS_GREATER(decodeNatural(2))(decodeNatural(4)),FALSE)

    def test_IS_LOWER_OR_EQUAL(self):
        self.assertEqual(IS_LOWER_OR_EQUAL(decodeNatural(2))(decodeNatural(4)),TRUE)

    def test_IS_LOWER(self):
        self.assertEqual(IS_LOWER(decodeNatural(2))(decodeNatural(4)),TRUE)

    def test_IS_EQUAL(self):
        self.assertEqual(IS_EQUAL(decodeNatural(4))(decodeNatural(4)),TRUE)

    def test_MIN(self):
        self.assertEqual(encodeNatural(MIN(decodeNatural(2))(decodeNatural(4))),2)

    def test_MAX(self):
        self.assertEqual(encodeNatural(MAX(decodeNatural(2))(decodeNatural(4))),4)

    def test_NEGATE(self):
        self.assertEqual(encodeSigned(NEGATE(decodeSigned(-10))),10) 
    
    def test_IS_POSITIVE(self):
        self.assertEqual(IS_POSITIVE(decodeSigned(-10)),FALSE) 
    
    def test_IS_NEGATIVE(self):
        self.assertEqual(IS_NEGATIVE(decodeSigned(-10)),TRUE) 

    def test_SIGNED_ADD(self):
        self.assertEqual(encodeSigned(SIGNED_ADD(decodeSigned(-10))(decodeSigned(-5))),-15) 

    def test_SIGNED_SUBTRACT(self):
        self.assertEqual(encodeSigned(SIGNED_SUBTRACT(decodeSigned(-10))(decodeSigned(-5))),-5) 

    def test_SIGNED_MULTIPLY(self):
        self.assertEqual(encodeSigned(SIGNED_MULTIPLY(decodeSigned(-10))(decodeSigned(-5))),50) 

    def test_SIGNED_DIVIDE(self):
        self.assertEqual(encodeSigned(SIGNED_DIVIDE(decodeSigned(-10))(decodeSigned(-5))),2) 