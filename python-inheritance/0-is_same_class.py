"""Module for checking object class."""

def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class; otherwise False.
    """
    return type(obj) is a_class

# Example usage:
class ExampleClass:
    pass

obj = ExampleClass()
result = is_same_class(obj, ExampleClass)

