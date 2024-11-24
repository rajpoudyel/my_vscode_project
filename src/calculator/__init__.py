#This file initializes the `calculator` package.
# Import all operations to make them accessible from the package level
from .add import add
from .subtract import subtract
from .multiply import multiply
from .divide import divide

__all__ = ["add", "subtract", "multiply", "divide"]