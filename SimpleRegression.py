import BasicStats


# Outputs the slope and intercept for the line of best fit for given data
# Input: Two datasets of equal length
# Output: Array containing regression coefficients: [slope, intercept]
def model(x_arr, y_arr):
    slope = BasicStats.correlation(x_arr, y_arr) * BasicStats.stdev(y_arr, False) / BasicStats.stdev(x_arr, False)
    x_mean = BasicStats.mean(x_arr)
    y_mean = BasicStats.mean(y_arr)
    intercept = y_mean - (slope * x_mean)
    return [slope, intercept]
