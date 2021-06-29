import unittest
import MultipleRegression


class MultipleRegressionTest(unittest.TestCase):
    def test_multiply(self):
        a = [[0, 2, 3], [3, 1, 3]]
        b = [[4, 8, 3, 2], [2, 9, 4, 5], [5, 6, 7, 8]]
        e = [[1], [2], [3], [4]]
        ab = [[19, 36, 29, 34], [29, 51, 34, 35]]
        be = [[37], [52], [70]]
        self.assertEqual(MultipleRegression.multiply(a, b), ab)  # Different dimensions 1
        self.assertEqual(MultipleRegression.multiply(b, e), be)  # Different dimensions 2
        c = [[3, 4, 5], [1, 2, 3], [4, 5, 6]]
        d = [[5, 4, 3], [2, 1, 3], [1, 2, 3]]
        cd = [[28, 26, 36], [12, 12, 18], [36, 33, 45]]
        dc = [[31, 43, 55], [19, 25, 31], [17, 23, 29]]
        self.assertEqual(MultipleRegression.multiply(c, d), cd)  # Same dimensions 1
        self.assertEqual(MultipleRegression.multiply(d, c), dc)  # Same dimensions 2

    def test_multiply_error(self):
        a = [[0, 2, 3], [3, 1, 3]]
        b = [[4, 8, 3, 2], [2, 9, 4, 5], [5, 6, 7, 8]]
        with self.assertRaises(RuntimeError):
            MultipleRegression.multiply(b, a)

    def test_transpose(self):
        c = [[3, 4, 5], [1, 2, 3], [4, 5, 6]]
        d = [[5, 4, 3], [2, 1, 3], [1, 2, 3]]
        c_transpose = [[3, 1, 4], [4, 2, 5], [5, 3, 6]]
        d_transpose = [[5, 2, 1], [4, 1, 2], [3, 3, 3]]
        self.assertEqual(MultipleRegression.transpose(c), c_transpose)  # Square matrix 1
        self.assertEqual(MultipleRegression.transpose(d), d_transpose)  # Square matrix 2
        a = [[0, 2, 3], [3, 1, 3]]
        b = [[4, 8, 3, 2], [2, 9, 4, 5], [5, 6, 7, 8]]
        a_transpose = [[0, 3], [2, 1], [3, 3]]
        b_transpose = [[4, 2, 5], [8, 9, 6], [3, 4, 7], [2, 5, 8]]
        self.assertEqual(MultipleRegression.transpose(a), a_transpose)  # Non-square matrix 1
        self.assertEqual(MultipleRegression.transpose(b), b_transpose)  # Non-square matrix 2

    def test_two_predictors(self):
        x_data = [[3, 8], [3, 5], [5, 7], [4, 6]]
        z_data = [[3], [4], [7], [4]]
        coeffs = MultipleRegression.regression(x_data, z_data)
        self.assertAlmostEqual(coeffs[0], -0.666666666)  # Intercept
        self.assertAlmostEqual(coeffs[1], 1.6666666666)  # Coefficient 1
        self.assertAlmostEqual(coeffs[2], -0.166666666)  # Coefficient 2

    def test_three_predictors(self):
        x_data = [[3, 8, 3], [3, 5, 8], [2, 6, 0], [5, 5, 5], [6, 3, 4]]
        y_data = [[4], [2], [10], [1], [2]]
        coeffs = MultipleRegression.regression(x_data, y_data)
        self.assertAlmostEqual(coeffs[0], 18.52857978)  # Intercept
        self.assertAlmostEqual(coeffs[1], -1.7593640265)  # Coefficient 1
        self.assertAlmostEqual(coeffs[2], -0.83027701911)  # Coefficient 2
        self.assertAlmostEqual(coeffs[3], -0.8898751463129)  # Coefficient 3

    def test_convert_to_equation(self):
        x_data = [[3, 8], [3, 5], [5, 7], [4, 6]]
        z_data = [[3], [4], [7], [4]]
        coeffs = MultipleRegression.regression(x_data, z_data)
        equation = MultipleRegression.convert_to_equation(coeffs)
        self.assertEqual(equation, "y = -0.6666666666666679 + 1.6666666666666667(x1) + 0.16666666666666763(x2) ")


if __name__ == '__main__':
    unittest.main()
