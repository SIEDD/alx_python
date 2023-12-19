def raise_exception_msg():
    raise NameError("C is fun")
try:
    raise_exception_msg()
except NameError as e:
    print(e)


