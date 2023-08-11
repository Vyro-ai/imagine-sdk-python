from abc import ABC, abstractmethod
from typing import Optional, Dict, Tuple, Union


class HttpClient(ABC):
    """
    Interface for http clients.
    """

    @abstractmethod
    def post(
        self,
        endpoint: str,
        parameters: Dict[str, Union[int, float, str]],
        files: Optional[Dict[str, bytes]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Tuple[int, bytes]:
        """
        Perform an HTTP POST request to the specified endpoint.

        This method sends an HTTP POST request to the given endpoint with the
        provided parameters and optional files.

        :param endpoint: The API endpoint to which the request is made.
        :type endpoint: str
        :param parameters: The data parameters to include in the request.
        :type parameters: Dict[str, Union[int, float, str]]
        :param files: Files to be uploaded along with the request.
        :type files: Optional[Dict[str, bytes]]
        :param headers: Custom headers to include in the request.
        :type headers: Dict[str, str], optional
        :return: A tuple containing the HTTP response status code and the
            response content (bytes) received from the server.
        :rtype: Tuple[int, bytes]
        """
        raise NotImplementedError("Subclasses must implement this method.")
