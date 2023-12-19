def update_dictionary(a_dictionary, key, value):
    # Update or add the key-value pair in the dictionary
    a_dictionary[key] = value

# Example usage:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Update existing key
update_dictionary(my_dict, 'age', 26)

# Add a new key-value pair
update_dictionary(my_dict, 'gender', 'Male')

print(my_dict)

