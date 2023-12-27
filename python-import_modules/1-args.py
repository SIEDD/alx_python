import sys
if __name__ == "__main__":
    def print_arguments():
        num_arguments = len(sys.argv) - 1
        print(num_arguments, end=" ")
        if num_arguments == 1:
            print("argument:",end="")
        elif num_arguments > 1:
            print("arguments:",end="")
        else:
            print(".", end="")
        return

    for i, arg in enumerate(sys.argv[1:],start=1):
        print("\n{}: {}".format(i, arg))






