import numpy as np
import math 
import unittest

def square(x):
    return x*x

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def test_is_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is prime({n}), expected {expected} got {is_prime(n)}")


if __name__ == '__main__':
    print(square(10))
    assert square(10) == 100


class Tests(unittest.TestCase):
    def test_1(self):
        """ Check that 1 is prime """
        self.assertFalse(is_prime(1))
    def test_2(self):
        """ Check that 2 is prime """
        self.assertTrue(is_prime(2))


if __name__ == '__main__':
    print(square(10))
    assert square(10) == 100
    unittest.main()