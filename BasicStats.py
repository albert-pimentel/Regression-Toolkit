

# Returns the mean of a list of data
# Runtime: O(n)
def mean(arr):
    total = 0
    for i in arr:
        total += i
    return total / len(arr)


# Returns the median of a list of data
# Runtime: O(nlgn)
# To-do: Improve to O(n) via select algorithm
def median(arr):
    sorted_arr = sorted(arr)
    length = len(sorted_arr)
    if length % 2 == 1:
        return arr[length // 2]
    return (sorted_arr[(length // 2) - 1] + sorted_arr[length // 2]) / 2


# Returns the standard deviation of a list of data
# Runtime: O(n)
def stdev(arr):
    avg = mean(arr)
    sqr_residuals = 0
    for i in arr:
        sqr_residuals += (i - avg)**2
    return (sqr_residuals / (len(arr) - 1))**(1/2)


# Returns the correlation between two data sets of equal length
# Runtime: O(n)
def correlation(x_arr, y_arr):
    if len(x_arr) != len(y_arr):
        raise RuntimeError("Data sets must be of equal length")
    residual_product = 0
    x_mean = mean(x_arr)
    y_mean = mean(y_arr)
    x_stdev = stdev(x_arr)
    y_stdev = stdev(y_arr)
    for i in range(len(x_arr)):
        x_residual = (x_arr[i] - x_mean) / x_stdev
        y_residual = (y_arr[i] - y_mean) / y_stdev
        residual_product += x_residual * y_residual
    return residual_product / (len(x_arr) - 1)


# Returns the range of a list of data
# Runtime: O(n)
def data_range(arr):
    return max(arr) - min(arr)


# Returns the mode(s) of a list of data
# Runtime: O(n)
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


print("Mean: " + str(mean([7, 10, 13])))  # Should be 10
print("Median: " + str(median([7, 10, 13, 15])))  # Should be 11.5 (sorted)
print("Median: " + str(median([10, 13, 15, 7])))  # Should be 11.5 (unsorted)
print("Stdev: " + str(stdev([1, 2, 3, 4, 5])))  # Should be 1.5811
print("Correlation: " + str(correlation([7, 3, 1, 30, 10], [10, 14, -1, 5, 9])))  # Should be -0.118
print("Range: " + str(data_range([50, 10, 4, 20, 5, 2])))  # Should be 48
print("Modes: " + str(mode([5, 5, 10, 12, 4, 4, 4, 12, 10, 8, 7, 5])))  # Should be [5, 4]
print("Modes: " + str(mode([5, 10, 12, 4, 4, 4, 12, 10, 8, 7, 5])))  # Should be [4]
