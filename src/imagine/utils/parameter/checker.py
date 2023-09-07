from typing import Any, Dict, Optional


def parameter_builder(**kwargs: Any) -> Dict[str, Any]:
    """
    Build a dictionary by removing null values from the given parameters.

    This utility function constructs a dictionary by iterating through the
    key-value pairs in the provided keyword arguments and including only the
    non-null values in the resulting dictionary.

    :param `**kwargs`: Keyword arguments with keys as strings and values of any type.
    :type `**kwargs`: Any
    :return: A dictionary containing non-null key-value pairs.
    :rtype: Dict[str, Any]

    Usage:
        >>> params = parameter_builder(name="John", age=None, city="New York")
        >>> print(params)Ï
        {'name': 'John', 'city': 'New York'}
    """
    return {k: v for (k, v) in kwargs.items() if v is not None}


def non_optional_parameter_checker(**kwargs: Any) -> Optional[ValueError]:
    """
    Check for non-optional parameters and return a ValueError if any is None.

    This function examines the provided keyword arguments and checks if any
    of the values are None. If any value is None, it raises a ValueError
    indicating that the parameter cannot be null.

    :param `**kwargs`: Keyword arguments with keys as strings and values of any type.
    :type `**kwargs`: Any
    :return: A ValueError if any parameter value is None, otherwise None.
    :rtype: Optional[ValueError]

    Usage:
        >>> error = non_optional_parameter_checker(name="Alice", age=None,
            city="London")
        >>> if error:
        ...     raise error
    """
    for key, val in kwargs.items():
        if val is None:
            return ValueError(
                f"Parameter '{key}' cannot be null. Please make"
                + "sure you are passing a valid value."
            )
    return None
