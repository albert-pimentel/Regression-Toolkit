import BasicStats


# Outputs the slope and intercept for the line of best fit for given data
# Input: Two datasets of equal length
# Output: Array containing regression coefficients: [slope, intercept]
# Runtime: O(n)
def model(xArr, yArr):
    slope = BasicStats.correlation(xArr, yArr) * BasicStats.stdev(yArr, False) / BasicStats.stdev(xArr, False)
    xMean = BasicStats.mean(xArr)
    yMean = BasicStats.mean(yArr)
    intercept = yMean - (slope * xMean)
    return [slope, intercept]
