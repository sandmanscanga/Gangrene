"""
Module to test submodule1 of gangrene.

Summary:
    This module contains tests for submodule1 of gangrene. It
    demonstrates how to write tests for submodule1 using the pytest
    framework.

Example:
    To run the tests for submodule1 of gangrene, use the following
    command:

    $ pytest tests/test_submodule1.py

    The command runs the tests for submodule1 of gangrene using the
    pytest framework.

"""

from gangrene.submodule1.helper import helper_function


def test_helper_function() -> None:
    """
    Test the helper_function of submodule1.

    Summary:
        This test checks the helper_function of submodule1. It
        demonstrates how to write tests for the helper_function
        using the pytest framework.

    """

    assert helper_function() == "This is a helper function from submodule1."
