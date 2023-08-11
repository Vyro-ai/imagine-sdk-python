from typing import Optional, TypeVar


E = TypeVar("E", bound=BaseException)


def check_and_raise(exception: Optional[E]):
    """
    Check and raise the provided exception if not None.

    :param exception: An optional exception instance to be raised.
    :type exception: Optional[Type[BaseException]]
    :raises: E: If the provided exception is not None.
    
    Usage:
        >>> try:
        ...     # Some code that may raise an exception
        ... except SomeException as se:
        ...     check_and_raise(se)
    """
    if exception is not None:
        raise exception
