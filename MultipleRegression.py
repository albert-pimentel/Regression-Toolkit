
import numpy

# In computing the multiple regression coefficients, inputted data is
# assumed to be in the form of a 2D array (list) in which the final column
# contains the values for the response variable.

# Since there must be more observations than explanatory variables for the
# model to work, number of rows must be greater than number of columns


# Multiplies two matrices
# ([r x k] * [k x c] -> [r x c])
# Runtime: O(k^3)
def multiply(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix):
        raise RuntimeError("Matrices must have shared dimension")
    # Create new matrix of appropriate size
    rows = len(first_matrix)
    columns = len(second_matrix[0])
    shared_dimension = len(first_matrix[0])
    new_matrix = [[0 for i in range(columns)] for j in range(rows)]
    # Fill in cells
    for i in range(shared_dimension):
        for j in range(shared_dimension):
            sum_products = 0
            for z in range(shared_dimension):
                sum_products += first_matrix[i][z] * second_matrix[z][j]
            new_matrix[i][j] = sum_products
    return new_matrix


# Transposes a matrix
# Runtime: O(nm)
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
# An alternative (but inefficient on large matrices) solution is to manually implement inversion by cofactors
# Runtime: O(n^3)
def inverse(matrix):
    return numpy.linalg.pinv(matrix)


# Outputs a [k x 1] array containing multiple regression coefficients
# Explanatory data must a [n x k] array
# Response data must be a [n x 1] array, n > k
# Runtime:
def multiple_regression(explanatory_data, response_data):
    if len(explanatory_data) != len(response_data):
        raise RuntimeError("Must be one response per row of explanatory data")
    t_explanatory = transpose(explanatory_data)
    inverted = inverse(multiply(t_explanatory, explanatory_data))
    coeffs = multiply(multiply(inverted, t_explanatory), response_data)
    return coeffs


matrix_a = [[0, 2], [3, 1]]
matrix_b = [[4, 8], [2, 9]]
matrix_c = [[3, 4, 5], [1, 2, 3], [4, 5, 6]]
matrix_d = [[3, 4, 5], [1, 2, 3], [1, 2, 3]]
matrix_e = [[2, 5], [3, 7], [4, 5]]
test_matrix1 = multiply(matrix_a, matrix_b)
test_matrix2 = multiply(matrix_c, matrix_d)
test_matrix3 = transpose(matrix_c)
test_matrix4 = transpose(matrix_e)
print(test_matrix1)
print(test_matrix2)
print(test_matrix3)
print(test_matrix4)

x_data = [[3, 2], [3, 5], [2, 6]]
y_data = [[4], [2], [2]]
coefficients = multiple_regression(x_data, y_data)
print(coefficients)
