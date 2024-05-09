"""
Module to demonstrate the use of __init__.py file in a package.

Summary:
    This module demonstrates the use of the __init__.py file in a
    package. It provides a simple class to demonstrate the main
    functionality of the gangrene package.

Classes:
    MainClass: A simple class to demonstrate the main functionality
        of the gangrene package.

Example:
    To use the MainClass class, import it from the gangrene package:

    >>> from gangrene import MainClass
    >>> main = MainClass()
    >>> main.greet()
    'Hello from MainClass!'

"""


class MainClass:
    """
    Class to demo the main functionality of the gangrene package.

    Summary:
        This class provides a simple method to greet the user. It
        demonstrates the main functionality of the gangrene package.
        The class can be used to demonstrate the use of the
        __init__.py file in a package. The class can be imported
        from the gangrene package.

    Attributes:
        message (str): A string containing the main functionality of
            the gangrene package.

    Methods:
        greet: A method to greet the user.

    Example:
        To use the MainClass class, import it from the gangrene package:

        >>> from gangrene import MainClass
        >>> main = MainClass()

        To greet the user, use the greet method:

        >>> main.greet()
        'Hello from MainClass!'

    """

    def __init__(self) -> None:
        """
        Initialize the MainClass object.

        Summary:
            This method initializes the MainClass object. It sets
            the message attribute to a string containing the main
            functionality of the gangrene package.

        """

        self.message = "Main functionality of the gangrene package."

    def greet(self) -> str:
        """
        Greet the user.

        Summary:
            This method greets the user with a message. It returns
            a string containing the greeting message.

        Returns:
            str: A string containing the greeting message.

        Example:
            To greet the user, use the greet method:

            >>> main = MainClass()
            >>> main.greet()
            'Hello from MainClass!'

        """

        return "Hello from MainClass!"
