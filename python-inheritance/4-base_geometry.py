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
        raise Exception("area() is not implemented.")
