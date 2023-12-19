def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set = set()

    # Iterate through elements in set_1
    for elem in set_1:
        # Check if the element is in set_2
        if elem in set_2:
            # Add the common element to the common_set
            common_set.add(elem)

    # Return the set of common elements
    return common_set

# Example usage:
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}

# result = common_elements(set_1, set_2)
# print(result)

