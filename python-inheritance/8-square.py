"""importing from Rectangle"""
Rectangle = __import__('7-rectangle').Rectangle
"""class containing square"""
class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
    """implementing the area"""
    def area(self):
        return self.__size * self.__size    