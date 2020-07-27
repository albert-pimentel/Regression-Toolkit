import numpy

# In computing the multiple regression coefficients, inputted data is
# assumed to be in the form of a 2D array (list) in which the final column
# contains the values for the response variable.

# Since there must be more observations than explanatory variables for the
# model to work, number of rows must be greater than number of columns


# Multiplies two matrices
# Input: Two matrices of multiplicable dimensions ([r x k] * [k x c] -> [r x c])
# Output: Product of two matrices
# Runtime: O(k^3)
def multiply(firstMatrix, secondMatrix):
    if len(firstMatrix[0]) != len(secondMatrix):
        raise RuntimeError("Matrices must have shared dimension")
    # Create new matrix of appropriate size
    rows = len(firstMatrix)
    columns = len(secondMatrix[0])
    sharedDimension = len(firstMatrix[0])
    newMatrix = [[0 for c in range(columns)] for r in range(rows)]
    # Fill in cells
    for i in range(rows):
        for j in range(columns):
            sumProducts = 0
            for z in range(sharedDimension):
                sumProducts += firstMatrix[i][z] * secondMatrix[z][j]
            newMatrix[i][j] = sumProducts
    return newMatrix


# Transposes a matrix
# Input: A matrix
# Output: Transpose of matrix
# Runtime: O(nm)
def transpose(matrix):
    # Create new matrix of appropriate size
    # [m x n] -> [n x m]
    rows = len(matrix[0])
    columns = len(matrix)
    newMatrix = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(columns):
        for j in range(rows):
            newMatrix[j][i] = matrix[i][j]
    return newMatrix


# Utilizes Numpy's built-in pseudo-inverse function, which gives an approximate
# inverse in the event the matrix is not invertible
# A manual solution (but inefficient on large matrices) is to implement inversion by cofactors
# Input: A matrix
# Output: Inverted (or approximately inverted) matrix
# Runtime: O(n^3)
def inverse(matrix):
    return numpy.linalg.inv(matrix)


# Computes multiple regression coefficients given 2D array representation of data
# Input: Explanatory data as an [n x k] array, response data as an [n x 1] array, n > K
# Output: [1 x (k+1)] array containing multiple regression coefficients
#         Index 0 is the intercept, indices 1 to k contain coefficients
# Runtime: O(n^3)
def regression(explanatoryData, responseData):
    if len(explanatoryData) != len(responseData):
        raise RuntimeError("Must have one response per row of explanatory data")
    # Add leftmost column of 1s
    for i in range(len(explanatoryData)):
        explanatoryData[i].insert(0, 1)
    # Calculate coefficient matrix
    tExplanatory = transpose(explanatoryData)
    multiplied = multiply(tExplanatory, explanatoryData)
    inverted = inverse(multiplied)
    coeffMatrix2d = multiply(multiply(inverted, tExplanatory), responseData)
    # Coeff matrix is currently in form of 2D array, but can be represented
    # as a 1D array
    coeffMatrix = [0 for i in range(len(coeffMatrix2d))]
    for i in range(len(coeffMatrix)):
        coeffMatrix[i] = coeffMatrix2d[i][0]
    return coeffMatrix


# Converts coefficient matrix to presentable equation
# Input: Array of length n containing regression coefficients
# Output: String representation of multiple regression model
# Runtime: O(n)
def convertToEquation(coeffMatrix):
    str_coeffs = " + "
    for j in range(1, len(coeffMatrix)):
        coeff = coeffMatrix[j]
        sign = "+"
        if coeff < 0:
            sign = "-"
        if j == len(coeffMatrix) - 1:
            str_coeffs += str(abs(coeff)) + "(x" + str(j) + ") "
        else:
            str_coeffs += str(abs(coeff)) + "(x" + str(j) + ") " + sign + " "
    return "y = " + str(coeffMatrix[0]) + str_coeffs
