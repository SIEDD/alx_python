def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

# Example usage:
original_list = [1, 2, 3, 4]
multiplier = 2
result = multiply_list_map(original_list, multiplier)
print(result)

