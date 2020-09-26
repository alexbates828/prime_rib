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

    def test_is_prime_with_range_by_with_mod_returns_false_for_zero(self):
        n = 0
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertFalse(result)

    def test_is_prime_with_range_by_with_mod_returns_false_for_one(self):
        n = 1
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertFalse(result)

    def test_is_prime_with_range_by_with_mod_returns_true_for_two(self):
        n = 2
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertTrue(result)

    def test_is_prime_with_range_by_with_mod_returns_true_for_three(self):
        n = 3
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertTrue(result)

    def test_is_prime_with_range_by_with_mod_returns_false_for_four(self):
        n = 4
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertFalse(result)

    def test_is_prime_with_range_by_with_mod_returns_false_for_composite(self):
        n = 169
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertFalse(result)

    def test_is_prime_with_range_by_with_mod_returns_false_for_second_composite(self):
        n = 144
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertFalse(result)

    def test_is_prime_with_range_by_with_mod_returns_true_for_prime_number(self):
        n = 101
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertTrue(result)

    def test_is_prime_with_range_by_with_mod_returns_true_for_negative_prime(self):
        n = -101
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertTrue(result)

    def test_is_prime_with_range_by_with_mod_returns_false_for_negative_composite(self):
        n = -1234321 #  1234321 = 1111 * 1111
        result = prime_utils.is_prime_with_range_by_with_mod(n)
        self.assertFalse(result)

    def test_range_by_with_mod_returns_all_nums_for_relatively_prime(self):
        n = 101
        b = 45
        gen = prime_utils.range_by_with_mod(n,b)
        l = list(gen)
        self.assertEqual(n, len(l))

    def test_range_by_with_mod_returns_zero_list_when_n_is_one(self):
        n = 1
        b = 45
        gen = prime_utils.range_by_with_mod(n,b)
        l = list(gen)
        self.assertEqual([0], l)


if __name__ == '__main__':
    unittest.main()
