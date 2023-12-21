"""importing Base"""
from models.base import Base
"""class contains rectangle properties"""
class Rectangle(Base):
    """Rectangle class inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle (default is 0).
            y (int, optional): y-coordinate of the rectangle (default is 0).
            id (int, optional): If provided, assign it to the public instance attribute id.
                               Otherwise, use the logic of the __init__ of the Base class to generate a new id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_non_negative_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_non_negative_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.validate_non_negative_int("y", value)
        self.__y = value
    """mehod for area of rectangle"""
    def area(self):
        """returns the width and height"""
        return self.__width * self.__height
    """method for displaying #sign"""
    def display(self):
        """output"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    """method for validating positive integer"""
    def validate_positive_integer(self, value, attribute):
        """raising type and value errors"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")    
    """method for validating non-negative integers"""
    def validate_non_negative_int(self, attribute, value):
        """Validate that the given value is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        elif value < 0:
            raise ValueError(f"{attribute} must be >= 0")
