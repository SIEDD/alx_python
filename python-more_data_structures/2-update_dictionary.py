def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

def print_sorted_dictionary(my_dict):
    """Print sorted dictionary"""
    keys = sorted(my_dict)
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))

if __name__ =='__main__':

    a_dictionary = {'language': "Cd", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)