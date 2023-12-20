"""This module provides functions to check class relationships."""

def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class

def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherited from, a_class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of or inherited from a_class; otherwise, False.
    """
    return isinstance(obj, a_class)

def inherits_from(obj, a_class):
    """Check if obj is an instance of a class inherited (directly or indirectly) from a_class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class inherited from a_class; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

