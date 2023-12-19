def update_dictionary(a_dictionary, key, value):
    # Update or add the key-value pair in the dictionary
    a_dictionary[key] = value

my_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

my_dict['a'] = 'A'
sentence = my_dict.split()
for i in my_dict:
    print(i)