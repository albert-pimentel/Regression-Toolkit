# Returns the mean of a list of data
# Input: Array of data
# Output: Mean of data
def mean(arr):
    total = 0
    for i in arr:
        total += i
    return total / len(arr)


# Returns the median of a list of data
# To-do: Improve to O(n) via select algorithm
# Input: Array of data
# Output: Median of data
def median(arr):
    arr = sorted(arr)
    length = len(arr)
    if length % 2 == 1:
        return arr[length // 2]
    return (arr[(length // 2) - 1] + arr[length // 2]) / 2


# Returns the standard deviation of a list of data
# Must input a boolean, population, which is true
# if stdev is for population, false for sample
# Input: Dataset (arr), boolean (population)
# Output: Standard deviation
def stdev(arr, population):
    avg = mean(arr)
    sqr_residuals = 0
    for i in arr:
        sqr_residuals += (i - avg)**2
    if population:
        return (sqr_residuals / (len(arr)))**(1/2)
    return (sqr_residuals / (len(arr) - 1))**(1/2)


# Returns the correlation between two data sets of equal length
# Input: Two datasets of equal length
# Output: Correlation between two datasets
def correlation(x_arr, y_arr):
    if len(x_arr) != len(y_arr):
        raise RuntimeError("Data sets must be of equal length")
    residual_product = 0
    x_mean = mean(x_arr)
    y_mean = mean(y_arr)
    x_stdev = stdev(x_arr, False)
    y_stdev = stdev(y_arr, False)
    for i in range(len(x_arr)):
        x_residual = (x_arr[i] - x_mean) / x_stdev
        y_residual = (y_arr[i] - y_mean) / y_stdev
        residual_product += x_residual * y_residual
    return residual_product / (len(x_arr) - 1)


# Returns the range of a list of data
# Input: Array of data
# Output: Max of data - min of data
def data_range(arr):
    return max(arr) - min(arr)


# Returns the mode(s) of a list of data
# Input: Array of data
# Output: Set of most frequently appearing numbers
def mode(arr):
    # Map each number in the data to its frequency
    freq = {}
    for entry in arr:
        freq[entry] = 0
    for entry in arr:
        freq[entry] += 1
    # Find the maximum frequency of any number in the data set
    max_freq = max(freq.values())
    # Return the set of keys mapped to maximum frequency
    modes = []
    for entry in freq.keys():
        if freq[entry] == max_freq:
            modes.append(entry)
    return modes
