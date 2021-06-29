import numpy

# In computing the multiple regression coefficients, inputted data is
# assumed to be in the form of a 2D array (list) in which the final column
# contains the values for the response variable.

# Since there must be more observations than explanatory variables for the
# model to work, number of rows must be greater than number of columns


# Multiplies two matrices
# Input: Two matrices of multiplicable dimensions ([r x k] * [k x c] -> [r x c])
# Output: Product of two matrices
def multiply(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix):
        raise RuntimeError("Matrices must have shared dimension")
    # Create new matrix of appropriate size
    rows = len(first_matrix)
    columns = len(second_matrix[0])
    shared_dimension = len(first_matrix[0])
    new_matrix = [[0 for c in range(columns)] for r in range(rows)]
    # Fill in cells
    for i in range(rows):
        for j in range(columns):
            sum_products = 0
            for z in range(shared_dimension):
                sum_products += first_matrix[i][z] * second_matrix[z][j]
            new_matrix[i][j] = sum_products
    return new_matrix


# Transposes a matrix
# Input: A matrix
# Output: Transpose of matrix
def transpose(matrix):
    # Create new matrix of appropriate size
    # [m x n] -> [n x m]
    rows = len(matrix[0])
    columns = len(matrix)
    new_matrix = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(columns):
        for j in range(rows):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


# Utilizes Numpy's built-in pseudo-inverse function, which gives an approximate
# inverse in the event the matrix is not invertible
# A manual solution (but inefficient on large matrices) is to implement inversion by cofactors
# Input: A matrix
# Output: Inverted (or approximately inverted) matrix
def inverse(matrix):
    return numpy.linalg.inv(matrix)


# Computes multiple regression coefficients given 2D array representation of data
# Input: Explanatory data as an [n x k] array, response data as an [n x 1] array, n > K
# Output: [1 x (k+1)] array containing multiple regression coefficients
#         Index 0 is the intercept, indices 1 to k contain coefficients
def regression(explanatory_data, response_data):
    if len(explanatory_data) != len(response_data):
        raise RuntimeError("Must have one response per row of explanatory data")
    # Add leftmost column of 1s
    for i in range(len(explanatory_data)):
        explanatory_data[i].insert(0, 1)
    # Calculate coefficient matrix
    t_explanatory = transpose(explanatory_data)
    multiplied = multiply(t_explanatory, explanatory_data)
    inverted = inverse(multiplied)
    coeff_matrix2d = multiply(multiply(inverted, t_explanatory), response_data)
    # Coeff matrix is currently in form of 2D array, but can be represented
    # as a 1D array
    coeff_matrix = [0 for i in range(len(coeff_matrix2d))]
    for i in range(len(coeff_matrix)):
        coeff_matrix[i] = coeff_matrix2d[i][0]
    return coeff_matrix


# Converts coefficient matrix to presentable equation
# Input: Array of length n containing regression coefficients
# Output: String representation of multiple regression model
def convert_to_equation(coeff_matrix):
    str_coeffs = " + "
    for j in range(1, len(coeff_matrix)):
        coeff = coeff_matrix[j]
        sign = "+"
        if coeff < 0:
            sign = "-"
        if j == len(coeff_matrix) - 1:
            str_coeffs += str(abs(coeff)) + "(x" + str(j) + ") "
        else:
            str_coeffs += str(abs(coeff)) + "(x" + str(j) + ") " + sign + " "
    return "y = " + str(coeff_matrix[0]) + str_coeffs
