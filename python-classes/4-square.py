"""
This module defines the Square class.

The Square class represents a square with a specified size.

Attributes:
    None

Methods:
    - __init__(self, size=0): Initializes a new instance of the Square class.
    - size (property): Gets or sets the size of the square.
    - area(self): Calculates and returns the area of the square.
    - my_print(self): Prints a visual representation of the square.
"""

class Square:
    """this class represents a square"""
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Using the setter to ensure validation during initialization

    @property
    def size(self):
        """
        Gets or sets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square.
        
        If the size is 0, prints an empty line. Otherwise, prints rows of '#' characters.

        Example:
        For a square of size 3:
        ###
        ###
        ###
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
