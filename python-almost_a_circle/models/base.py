# models/base.py

class Base:
    """Base class for other classes."""

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): If provided, assign it to the public instance attribute id.
                               Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

