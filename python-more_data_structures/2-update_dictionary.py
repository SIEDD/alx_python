# def print_sorted_dictionary(my_dict):
#     if my_dict is not None:
#         keys = sorted(my_dict.keys())
#         for key in keys:
#             print("{}: {}".format(key, my_dict[key]))

# # Example usage
# my_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}
# print_sorted_dictionary(my_dict, 'a', 'A')
# print(my_dict)

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

my_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

update_dictionary(my_dict, 'a', 'A')
update_dictionary(my_dict, 'f', 'f')

for k, v in my_dict.items():
    print(f"{k}: {v}")

print("xx")




