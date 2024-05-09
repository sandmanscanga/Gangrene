"""
Module to test the main_module.py module.

Summary:
    This module contains tests for the main_module.py module. It
    demonstrates how to write tests for the main_module.py module
    using the pytest framework.

Example:
    To run the tests for the main_module.py module, use the
    following command:

    $ pytest tests/test_main_module.py

    The command runs the tests for the main_module.py module using
    the pytest framework.

"""

from gangrene.main_module import MainClass


def test_greet() -> None:
    """
    Test the greet method of the MainClass class.

    Summary:
        This test checks the greet method of the MainClass class. It
        demonstrates how to write tests for the greet method using
        the pytest framework.

    """

    obj = MainClass()

    assert obj.greet() == "Hello from MainClass!"
