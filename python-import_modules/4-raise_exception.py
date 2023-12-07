# def raise_exception():
#     raise TypeError("exception has been raised")

# # Example usage:
# raise_exception()

def raise_exception():
    raise TypeError("exception has been raised")

try:
    raise_exception()
except TypeError as e:
    print(e)
