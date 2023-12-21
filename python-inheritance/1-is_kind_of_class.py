"""This module provides a function to check if an object is an instance
   of, or inherited from, a specified class.
"""

def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherited from a_class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of, or inherited from, a_class; otherwise False.
    """
    return isinstance(obj, a_class)

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

