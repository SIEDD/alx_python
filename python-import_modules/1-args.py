import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    print(num_arguments, end=" ")

    # Print "argument" or "arguments" based on the number
    if num_arguments == 1:
        print("argument:", end="")
    elif num_arguments > 1:
        print("arguments:", end="")
    else:
        print(".", end="")
        return

    # Print each argument along with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("\n{}:{}".format(i, arg))

if __name__ == "__main__":
    print_arguments()

# def print_arguments():
#     num_arguments = len(sys.argv) - 1

#     # Print the number of arguments
#     print("{} argument{}:".format(num_arguments, "s" if num_arguments != 1 else ""), end=" ")

#     # Print each argument along with its position
#     for i, arg in enumerate(sys.argv[1:], start=1):
#         print("\n{}: {}".format(i, arg))

# if __name__ == "__main__":
#     print_arguments()
