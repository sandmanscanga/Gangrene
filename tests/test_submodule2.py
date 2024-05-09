"""
Module to test submodule2.

Summary:
    This module contains tests for submodule2 of gangrene. It
    demonstrates how to write tests for submodule2 using the pytest
    framework.

Example:
    To run the tests for submodule2 of gangrene, use the following
    command:

    $ pytest tests/test_submodule2.py

    The command runs the tests for submodule2 of gangrene using the
    pytest framework.

"""

from gangrene.submodule2.processor import process_data


def test_process_data() -> None:
    """
    Test the process_data function of submodule2.

    Summary:
        This test checks the process_data function of submodule2. It
        demonstrates how to write tests for the process_data
        function using the pytest framework.

    """

    assert process_data("test data") == "Processing data: test data"
