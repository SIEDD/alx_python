#def raise_exception():
#     raise TypeError("exception")

# # Example usage:
# raise_exception()
try:
    alist = [1,2,3]
    print(alist[3])

except IndexError:
    print("exception has been raised")
