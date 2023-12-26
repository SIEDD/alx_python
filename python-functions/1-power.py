# def pow(a, b):
#     result = 1
#     for _ in range(b):
#         result *= a
#     return result


def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

result = pow(0.01, 2)
print(result)
