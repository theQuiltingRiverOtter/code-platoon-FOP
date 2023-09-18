import unittest
import multiply


class testMultiply(unittest.TestCase):
    def test_std(self):
        product = multiply.multiply_3_numbers(3, 3, 3)
        self.assertEqual(product, 27)

    def test_notEqual(self):
        product = multiply.multiply_3_numbers(2, 2, 2)
        self.assertNotEqual(product, 1)

    def test_negatives(self):
        product = multiply.multiply_3_numbers(-2, -1, -3)
        self.assertEqual(product, -6)

    def test_floats(self):
        product = multiply.multiply_3_numbers(1.5, 2, 3.3)
        self.assertAlmostEqual(product, 9.9)

    def test_float_and_neg(self):
        product = multiply.multiply_3_numbers(2.333, -1, 1000)
        self.assertAlmostEqual(product, -2333)

    def test_large_nums(self):
        product = multiply.multiply_3_numbers(100, 233, 4321)
        self.assertEqual(product, 100679300)


if __name__ == "__main__":
    unittest.main()
