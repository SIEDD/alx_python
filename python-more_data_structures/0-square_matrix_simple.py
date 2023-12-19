def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store squared values for the current row
        squared_row = []

        # Iterate through each element in the current row and square it
        for element in row:
            squared_row.append(element ** 2)

        # Add the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix

# Example usage:
# input_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = square_matrix_simple(input_matrix)
# print(result)

