"""importing from rectangle class"""
from models.rectangle import Rectangle
"""the square class which has rectangle attributes"""
class Square(Rectangle):
    """super method"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value    
    """str method"""
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

