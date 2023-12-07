# script.py

import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    print("Number of argument(s):", num_arguments, end=" ")

    # Print "argument" or "arguments" based on the number
    if num_arguments == 1:
        print("argument:", end=" ")
    elif num_arguments > 1:
        print("arguments:", end=" ")
    else:
        print(".", end="\n")
        return

    # Print each argument along with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("\n{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()

# # my_program.py
# import sys

# def print_arguments():
#     # Get the number of arguments
#     num_arguments = len(sys.argv) - 1  # Exclude the script name

#     # Print the header
#     if num_arguments == 0:
#         print("0 arguments.")
#         print(".")
#     elif num_arguments == 1:
#         print("1 argument:")
#     else:
#         print("{} arguments:".format(num_arguments))

#     # Print each argument
#     for i in range(1, num_arguments + 1):
#         print("{}: {}".format(i, sys.argv[i]))

# if __name__ == "__main__":
#     print_arguments()
