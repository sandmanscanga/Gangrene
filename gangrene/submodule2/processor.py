"""
This is a module that processes data.

Summary:
    This module contains a function that processes data. The
    function takes a single argument, `data`, and returns a string
    indicating that the data is being processed.

Attributes:
    None

Example:
    To process some data, use the `process_data` function:

    >>> process_data("some data")
    'Processing data: some data'

    The example processes some data and returns a string indicating
    that the data is being processed.

"""


def process_data(data: str) -> str:
    """
    Process some data.

    Summary:
        This function processes some data. It takes a single
        argument, `data`, and returns a string indicating that the
        data is being processed.

    Args:
        data (str): The data to process.

    Returns:
        str: A message indicating that the data is being processed.

    Example:
        To process some data, call the function as follows:

        >>> process_data("some data")
        'Processing data: some data'

        The example processes some data and returns a string
        indicating that the data is being processed.

    """

    return f"Processing data: {data}"
