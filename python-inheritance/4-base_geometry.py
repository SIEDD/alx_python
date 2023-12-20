class BaseGeometry:
    """A base class representing basic geometry."""
    
    def __init__(self):
        pass
    
    def area(self):
        """Raise an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented.")
    
    def __str__(self):
        """Return a string representation of the object."""
        return "BaseGeometry object"
