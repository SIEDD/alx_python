def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_index, element in enumerate(row):
            if col_index == len(row) - 1:
                # Last element in the row
                print("{:d}".format(element), end="")
            else:
                # Not the last element in the row
                print("{:d} ".format(element), end="")
        print()  # Move to the next line after each row

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)

