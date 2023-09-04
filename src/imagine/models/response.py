from typing import TypeVar, Generic, Optional
from .status import Status


T = TypeVar("T")


class Response(Generic[T]):
    """
    A generic response class that represents the result of an imaginary
    operation.

    This class is designed to encapsulate both the response data and the
    status of an operation.

    :param data: The optional data associated with the response.
    :type data: Optional[T]
    :param status: The status code of the operation.
    :type status: int
    """

    __data: Optional[T]
    __status: Status

    def __init__(self, data: Optional[T], status: int) -> None:
        self.__data: Optional[T] = data
        self.__status = Status(status)

    @property
    def status(self) -> Status:
        """
        Get the status of the response.

        :return: The status of the response.
        :rtype: :class:`Status`
        """
        return self.__status

    @property
    def data(self) -> Optional[T]:
        """
        Get the response data.

        :return: The response data, if available. Otherwise, None.
        :rtype: Optional[T]
        """
        return self.__data

    def get_or_throw(self) -> T:
        """
        Get the response data or raise an exception if data is not available.

        :return: The response data, if available.
        :rtype: T
        :raises ValueError: If data is not available in the response.
        """
        if self.__data is None:
            raise ValueError(
                "Response data is not available in the response object."
                + f" Status Resonse: {self.__status}"
            )

        return self.__data

    def get_or_else(self, default: T) -> T:
        """
        Get the response data or return the provided default value if data is
        not available.

        :param default: The default value to return if data is not available.
        :type default: T
        :return: The response data if available, otherwise the provided default
            value.
        """
        return self.__data if self.__data is not None else default
