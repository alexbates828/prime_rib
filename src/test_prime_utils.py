import unittest
import prime_utils


class TestPrimeUtils(unittest.TestCase):

    def test_is_prime_returns_false_for_zero(self):
        n = 0
        result = prime_utils.is_prime(n)
        self.assertFalse(result)

    def test_is_prime_returns_false_for_one(self):
        n = 1
        result = prime_utils.is_prime(n)
        self.assertFalse(result)

    def test_is_prime_returns_true_for_two(self):
        n = 2
        result = prime_utils.is_prime(n)
        self.assertTrue(result)

    def test_is_prime_returns_false_for_composite(self):
        n = 169
        result = prime_utils.is_prime(n)
        self.assertFalse(result)

    def test_is_prime_returns_false_for_second_composite(self):
        n = 144
        result = prime_utils.is_prime(n)
        self.assertFalse(result)

    def test_is_prime_returns_true_for_prime_number(self):
        n = 101
        result = prime_utils.is_prime(n)
        self.assertTrue(result)

    def test_is_prime_returns_true_for_negative_prime(self):
        n = -101
        result = prime_utils.is_prime(n)
        self.assertTrue(result)

    def test_is_prime_returns_false_for_negative_composite(self):
        n = -1234321 #  1234321 = 1111 * 1111
        result = prime_utils.is_prime(n)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
