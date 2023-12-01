import unittest
import main

class MyTestCase(unittest.TestCase):

    def testsort1(self):
        self.assertEqual(main.BubleSort([5, 4, 6, 3, 1]), [1, 3, 4, 5, 6])

    def testsort2(self):
        self.assertEqual(main.BubleSort([1, 2, 3, 4, 1]), [1, 1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
