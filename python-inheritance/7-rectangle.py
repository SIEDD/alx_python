""""importing basegeometry"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
"""class for rectangle"""
class Rectangle(BaseGeometry):
    """private method"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """implementing the area method"""
    def area(self):
        return self.__width * self.__height
    """returning rectangle description"""
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)   