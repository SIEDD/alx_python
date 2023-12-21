# """class representing a square"""
# class Square:
#     """A class representing a square.

#     Attributes:
#         __size (int): The size of the square.

#     Methods:
#         size() -> int: Getter method to retrieve the size of the square.
#     """

#     def __init__(self, size):
#         """Initialize a square with a given size."""
#         self.__size = size
    
#     @property
#     def size(self):
#         """Get the size of the square."""
#         return self.__size
"""class representing the square"""
class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        size() -> int: Getter method to retrieve the size of the square.
    """

    def __init__(self, size):
        """Initialize a square with a given size."""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

# Example usage
square = Square(3)
print(square.__class__)
print(square.__dict__)

