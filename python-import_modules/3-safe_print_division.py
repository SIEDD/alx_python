def safe_print_division(a, b):
    #try:
        result = a / b
    #except ZeroDivisionError:
        #print("Inside result: {}".format(None))
        #return None
   # else:
        print("Inside result: {}".format(result))
        return None
    #finally:
     #   print("Inside result: {}".format(None))

safe_print_division(10, 2)


# def safe_print_division(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Inside result: {}".format(None))
#         return None
#     else:
#         print("Inside result: {}".format(result))
#         return result
#     finally:
#         print("{a} / {b} = {}".format(result, a=a, b=b))

# safe_print_division(10, 2)


