import unittest

from fibonacci import fibonacci


class FibonacciTests(unittest.TestCase):
    def test_first_ten(self):
        self.assertEqual([fibonacci(n) for n in range(10)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_large_number(self):
        self.assertEqual(fibonacci(50), 12586269025)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_non_integer_input(self):
        for value in (1.5, "5", None, True):
            with self.subTest(value=value), self.assertRaises(TypeError):
                fibonacci(value)


if __name__ == "__main__":
    unittest.main()
