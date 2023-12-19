def print_sorted_dictionary(my_dict):
    if my_dict is not None:
        keys = sorted(my_dict.keys())
        for key in keys:
            print("{}: {}".format(key, my_dict[key]))

# Example usage
my_dict = {'a': 'A', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}
print_sorted_dictionary(my_dict)
