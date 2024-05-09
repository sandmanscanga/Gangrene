"""
Module to import all of the submodules for gangrene.

Summary:
    This module imports all of the submodules for the gangrene
    package. It provides a convenient way to import all of the
    submodules at once, making them available for use in other parts
    of the package.

Attributes:
    __all__ (list[str]): A list of strings containing the names of
        the submodules to import.

Example:
    To import all of the submodules for gangrene, use the following
    import statement:

    >>> from gangrene import *

    The example imports all of the submodules for gangrene, making
    them available for use in other parts of the package.

"""

from .main_module import MainClass
from .submodule1 import helper
from .submodule2 import processor

__all__ = ["MainClass", "helper", "processor"]
__version__ = "0.1.0"
