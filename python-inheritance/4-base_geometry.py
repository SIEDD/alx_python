"""Module: base_geometry

This module defines the BaseGeometry class, which represents basic geometry.

Classes:
    BaseGeometry: A base class for basic geometry operations.

Methods:
    area(self): Raises an exception indicating that area() is not implemented.
"""
class BaseGeometry:
    """A base class representing basic geometry.
    
    Attributes:
        None

    Methods:
        area(self): Raises an Exception indicating that area() is not implemented.
    """
    
    def area(self):
        """Raise an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
    def __dir__(self):
        return sorted(['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
                       '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', 
                       '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
                       '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area'
                       ])