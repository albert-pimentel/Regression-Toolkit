import unittest
import MultipleRegression


class MultipleRegressionTest(unittest.TestCase):
    def testMultiply(self):
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

    def testMultiplyError(self):
        a = [[0, 2, 3], [3, 1, 3]]
        b = [[4, 8, 3, 2], [2, 9, 4, 5], [5, 6, 7, 8]]
        with self.assertRaises(RuntimeError):
            MultipleRegression.multiply(b, a)

    def testTranspose(self):
        c = [[3, 4, 5], [1, 2, 3], [4, 5, 6]]
        d = [[5, 4, 3], [2, 1, 3], [1, 2, 3]]
        cTranspose = [[3, 1, 4], [4, 2, 5], [5, 3, 6]]
        dTranspose = [[5, 2, 1], [4, 1, 2], [3, 3, 3]]
        self.assertEqual(MultipleRegression.transpose(c), cTranspose)  # Square matrix 1
        self.assertEqual(MultipleRegression.transpose(d), dTranspose)  # Square matrix 2
        a = [[0, 2, 3], [3, 1, 3]]
        b = [[4, 8, 3, 2], [2, 9, 4, 5], [5, 6, 7, 8]]
        aTranspose = [[0, 3], [2, 1], [3, 3]]
        bTranspose = [[4, 2, 5], [8, 9, 6], [3, 4, 7], [2, 5, 8]]
        self.assertEqual(MultipleRegression.transpose(a), aTranspose)  # Non-square matrix 1
        self.assertEqual(MultipleRegression.transpose(b), bTranspose)  # Non-square matrix 2

    def testTwoPredictors(self):
        xData = [[3, 8], [3, 5], [5, 7], [4, 6]]
        zData = [[3], [4], [7], [4]]
        coeffs = MultipleRegression.regression(xData, zData)
        self.assertAlmostEqual(coeffs[0], -0.666666666)  # Intercept
        self.assertAlmostEqual(coeffs[1], 1.6666666666)  # Coefficient 1
        self.assertAlmostEqual(coeffs[2], -0.166666666)  # Coefficient 2

    def testThreePredictors(self):
        xData = [[3, 8, 3], [3, 5, 8], [2, 6, 0], [5, 5, 5], [6, 3, 4]]
        yData = [[4], [2], [10], [1], [2]]
        coeffs = MultipleRegression.regression(xData, yData)
        self.assertAlmostEqual(coeffs[0], 18.52857978)  # Intercept
        self.assertAlmostEqual(coeffs[1], -1.7593640265)  # Coefficient 1
        self.assertAlmostEqual(coeffs[2], -0.83027701911)  # Coefficient 2
        self.assertAlmostEqual(coeffs[3], -0.8898751463129)  # Coefficient 3

    def testConvertToEquation(self):
        xData = [[3, 8], [3, 5], [5, 7], [4, 6]]
        zData = [[3], [4], [7], [4]]
        coeffs = MultipleRegression.regression(xData, zData)
        equation = MultipleRegression.convertToEquation(coeffs)
        print(equation)
        self.assertEqual(equation, "y = -0.6666666666666679 + 1.6666666666666667(x1) + 0.16666666666666763(x2) ")


if __name__ == '__main__':
    unittest.main()
