def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherited from a_class."""
    return isinstance(obj, a_class)

# Example usage:
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

class AnotherClass:
    pass

obj1 = ParentClass()
obj2 = ChildClass()
obj3 = AnotherClass()

result1 = is_kind_of_class(obj1, ParentClass)
result2 = is_kind_of_class(obj2, ParentClass)
result3 = is_kind_of_class(obj3, ParentClass)

# print(result1)  # Output: True
# print(result2)  # Output: True
# print(result3)  # Output: False

