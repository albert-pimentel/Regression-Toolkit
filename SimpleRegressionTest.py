import unittest
import SimpleRegression


class SimpleRegressionTest(unittest.TestCase):
    def test_regression(self):
        slope = SimpleRegression.model([5, 10, 3, 50, 10, 2, 4, 8], [10, 12, 6, 44, 7, 30, 16, 14])[0]
        intercept = SimpleRegression.model([5, 10, 3, 50, 10, 2, 4, 8], [10, 12, 6, 44, 7, 30, 16, 14])[1]
        self.assertAlmostEqual(intercept, 10.21690340909)  # Intercept
        self.assertAlmostEqual(slope, 0.6224431818)  # Slope


if __name__ == '__main__':
    unittest.main()
