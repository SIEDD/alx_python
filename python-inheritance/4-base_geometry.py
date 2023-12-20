class BaseGeometry:
    """A base class representing basic geometry.

    Attributes:
        None

    Methods:
        area(): Raises an Exception indicating that area() is not implemented.
    """

    def area(self):
        """Raise an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

