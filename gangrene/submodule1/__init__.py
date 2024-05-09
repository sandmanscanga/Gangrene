"""
This is the __init__.py file for the submodule1 package.

Summary:
    This file is used to define the contents of the submodule1
    package. It imports the helper function from the helper module
    and makes it available for use in other parts of the package.

Attributes:
    __all__ (list[str]): A list of strings containing the names of
        the functions and classes to import.
    __version__ (str): A string containing the version number of the
        submodule1 package.

Example:
    To import the helper function from the submodule1 package, use
    the following import statement:

    >>> from submodule1 import helper_function

    The example imports the helper function from the submodule1
    package, making it available for use in other parts of the
    package.

"""

from .helper import helper_function

__all__ = ["helper_function"]
