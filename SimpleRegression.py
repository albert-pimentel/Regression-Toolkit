import BasicStats


# Outputs the line of best fit for two data sets in the form y = mx + b
# Runtime: O(n)
def simple_regression(x_arr, y_arr):
    slope = BasicStats.correlation(x_arr, y_arr) * BasicStats.stdev(y_arr) / BasicStats.stdev(x_arr)
    x_mean = BasicStats.mean(x_arr)
    y_mean = BasicStats.mean(y_arr)
    intercept = y_mean - (slope * x_mean)
    return "y = " + str(slope) + "x + " + str(intercept)


# Should be y = 0.6224x + 10.2169
print(simple_regression([5, 10, 3, 50, 10, 2, 4, 8], [10, 12, 6, 44, 7, 30, 16, 14]))
