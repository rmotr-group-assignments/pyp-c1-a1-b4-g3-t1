import unittest
from fibonacci import *


# this test will always fail because no fibonacci number is negative
def fib_failure(input):
    return -1

class FibonacciTestTemplate:
    
    # default setup will use a failing function in the tests
    # child classes should override this function with the fibonacci solver of
    # their choice
    def setUp(self):
        self.fib_solver = fib_failure

    def fib_check(self, n, expected_fib):
        self.assertEquals(self.fib_solver(n), expected_fib)

    def test_fib_simple_1(self):
        self.fib_check(0, 0)

    def test_fib_simple_2(self):
        self.fib_check(1, 1)

    def test_fib_simple_3(self):
        self.fib_check(2, 1)

    def test_fib_simple_4(self):
        self.fib_check(3, 2)

    def test_fib_simple_5(self):
        self.fib_check(10, 55)

    def test_fib_simple_6(self):
        self.fib_check(40, 102334155)

class TestRecursiveFib(FibonacciTestTemplate, unittest.TestCase):
    def setUp(self):
        self.fib_solver = recursive_fib

class TestIterativeFib(FibonacciTestTemplate, unittest.TestCase):
    def setUp(self):
        self.fib_solver = recursive_fib

class TestInputValidation(unittest.TestCase):
    
    def test_recursive_validator_1(self):
        self.assertTrue(validate_recursive_option("y"))

    def test_recursive_validator_2(self):
        self.assertTrue(validate_recursive_option("Y"))

    def test_recursive_validator_3(self):
        self.assertFalse(validate_recursive_option("n"))

    def test_recursive_validator_4(self):
        self.assertFalse(validate_recursive_option("N"))

    def test_recursive_validator_5(self):
        with self.assertRaises(ValueError):
            validate_recursive_option("apple")

    def test_recursive_validator_6(self):
        with self.assertRaises(ValueError):
            validate_recursive_option("never")

    def test_recursive_validator_7(self):
        with self.assertRaises(ValueError):
            validate_recursive_option("yorp")

    def test_fib_n_validator_1(self):
        self.assertEquals(validate_fib_n("13"), 13)

    def test_fib_n_validator_2(self):
        with self.assertRaises(ValueError):
            validate_fib_n("apple")

    def test_fib_n_validator_3(self):
        with self.assertRaises(ValueError):
            validate_fib_n("four")

    def test_fib_n_validator_2(self):
        with self.assertRaises(ValueError):
            validate_fib_n("10.5")

    def test_fib_n_validator_2(self):
        with self.assertRaises(ValueError):
            validate_fib_n("-5")

if __name__ == '__main__':
    unittest.main()
