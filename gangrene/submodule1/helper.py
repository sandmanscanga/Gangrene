"""
Module to demonstrate how to use helper functions in a submodule.

Summary:
    This module demonstrates how to use helper functions in a
    submodule. It provides a single helper function that can be
    imported and used in other parts of the package.

Example:
    To use the helper function from this submodule, use the
    following import statement:

    >>> from gangrene.submodule1 import HelperFunction

    The example imports the helper function from the submodule,
    making it available for use in other parts of the package.

"""


def helper_function() -> str:
    """
    A simple helper function.

    Summary:
        This function provides a simple helper function that can be
        used in other parts of the package. It does not take any
        arguments and does not return any values. It simply prints a
        message to the console. The function is intended to
        demonstrate how helper functions can be used in submodules.

    Args:
        None

    Returns:
        str: A message indicating that the helper function has
            been called.

    Example:
        To use the helper function, call it as follows:

        >>> helper_function()

        The example calls the helper function, which prints a
        message to the console.

    """

    return "This is a helper function from submodule1."
