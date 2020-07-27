

# Returns the mean of a list of data
# Input: Array of data
# Output: Mean of data
# Runtime: O(n)
def mean(arr):
    total = 0
    for i in arr:
        total += i
    return total / len(arr)


# Returns the median of a list of data
# To-do: Improve to O(n) via select algorithm
# Input: Array of data
# Output: Median of data
# Runtime: O(nlgn)
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
# Runtime: O(n)
def stdev(arr, population):
    avg = mean(arr)
    sqrResiduals = 0
    for i in arr:
        sqrResiduals += (i - avg)**2
    if population:
        return (sqrResiduals / (len(arr)))**(1/2)
    return (sqrResiduals / (len(arr) - 1))**(1/2)


# Returns the correlation between two data sets of equal length
# Input: Two datasets of equal length
# Output: Correlation between two datasets
# Runtime: O(n)
def correlation(xArr, yArr):
    if len(xArr) != len(yArr):
        raise RuntimeError("Data sets must be of equal length")
    residualProduct = 0
    xMean = mean(xArr)
    yMean = mean(yArr)
    xStdev = stdev(xArr, False)
    yStdev = stdev(yArr, False)
    for i in range(len(xArr)):
        xResidual = (xArr[i] - xMean) / xStdev
        yResidual = (yArr[i] - yMean) / yStdev
        residualProduct += xResidual * yResidual
    return residualProduct / (len(xArr) - 1)


# Returns the range of a list of data
# Input: Array of data
# Output: Max of data - min of data
# Runtime: O(n)
def dataRange(arr):
    return max(arr) - min(arr)


# Returns the mode(s) of a list of data
# Input: Array of data
# Output: Set of most frequently appearing numbers
# Runtime: O(n)
def mode(arr):
    # Map each number in the data to its frequency
    freq = {}
    for entry in arr:
        freq[entry] = 0
    for entry in arr:
        freq[entry] += 1
    # Find the maximum frequency of any number in the data set
    maxFreq = max(freq.values())
    # Return the set of keys mapped to maximum frequency
    modes = []
    for entry in freq.keys():
        if freq[entry] == maxFreq:
            modes.append(entry)
    return modes
