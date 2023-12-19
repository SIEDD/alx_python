def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

my_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

update_dictionary(my_dict, 'a', 'A')
update_dictionary(my_dict, 'f', 'f')

for k, v in my_dict.items():
    print(f"{k}: {v}")

print("xx")




