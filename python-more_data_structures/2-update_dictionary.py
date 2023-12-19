def update_dictionary(a_dictionary, key, value):
    # Update or add the key-value pair in the dictionary
    a_dictionary[key] = value

#Example usage:
my_dict = {'a': 'A', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

# Update existing key
update_dictionary(my_dict, 'a', 89)

# Add a new key-value pair
update_dictionary(my_dict, 'gender', 'Male')

print(my_dict)

