# main.py
from add_0 import add

def main():
    # Assign values to variables
    a = 1
    b = 2

    # Calculate the result using the imported add function
    result = add(a, b)

    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, result))

# Check if the script is run directly
if __name__ == "__main__":
    main()
