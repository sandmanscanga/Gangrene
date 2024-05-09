"""
This is the __init__.py file for the submodule2 package.

Summary:
    This file is used to define the contents of the submodule2
    package. It imports the processor function from the processor
    module and makes it available for use in other parts of the
    package.

Attributes:
    __all__ (list[str]): A list of strings containing the names of
        the functions and classes to import.

Example:
    To import the processor function from the submodule2 package,
    use the following import statement:

    >>> from submodule2 import process_data

    The example imports the processor function from the submodule2
    package, making it available for use in other parts of the
    package.

"""

from .processor import process_data

__all__ = ["process_data"]
