"""
This module defines the Square class.

The Square class represents a square with a specified size.

Attributes:
    None

Methods:
    - __init__(self, size=0): Initializes a new instance of the Square class.
    - area(self): Calculates and returns the area of the square.
"""
"""this class represents a square"""
class Square:
    """the class represents a square"""
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


