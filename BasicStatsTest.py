import unittest
import BasicStats


class BasicStatsTest(unittest.TestCase):
    def testMean(self):
        self.assertEqual(BasicStats.mean([2, 3, 10]), 5)  # Multiple data
        self.assertEqual(BasicStats.mean([1]), 1)  # Singleton

    def testMedian(self):
        self.assertEqual(BasicStats.median([1, 4, 2, 5, 3]), 3)  # Sorted
        self.assertEqual(BasicStats.median([1, 2, 3, 4, 5]), 3)  # Unsorted

    def testStdev(self):
        self.assertAlmostEqual(BasicStats.stdev([2, 3, 10], True), 3.559026084)  # Positive, population
        self.assertAlmostEqual(BasicStats.stdev([2, 3, 10], False), 4.35889894)  # Positive, sample
        self.assertAlmostEqual(BasicStats.stdev([-4, -3, -15], True), 5.43650214)  # Negative, population
        self.assertAlmostEqual(BasicStats.stdev([-4, -3, -15], False), 6.65832811)  # Negative, sample

    def testCorrelation(self):
        self.assertAlmostEqual(BasicStats.correlation([7, 3, 1, 30, 10], [10, 14, -1, 5, 9]), -0.100059626)
        self.assertAlmostEqual(BasicStats.correlation([10, 5, 20, 10, 60, 40, 20, 5, 6], [5, 2, 8, 2, 8, 1, 8, 3, 7]),
                               0.26331562222)

    def testRange(self):
        self.assertEqual(BasicStats.dataRange([10, 5, 20, 10]), 15)  # Positive range
        self.assertEqual(BasicStats.dataRange([-10, -5, -10, -5, -25]), 20)  # Negative range

    def testMode(self):
        self.assertEqual(BasicStats.mode([5, 5, 10, 12, 4, 4, 4, 12, 10, 8, 7, 5]), [5, 4])
        self.assertEqual(BasicStats.mode([5, 10, 12, 4, 4, 4, 12, 10, 8, 7, 5]), [4])


if __name__ == '__main__':
    unittest.main()
