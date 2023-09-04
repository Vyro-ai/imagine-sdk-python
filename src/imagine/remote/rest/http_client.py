from typing import Optional, Dict, Tuple, Union
from ..http_client import HttpClient
from .._imagine.http_client import RequestClient


class RestClient(HttpClient):
    """
    The RestClient class is responsible for making authenticated HTTP POST requests
    to the Imagine API using an authorization token. It does this by delegating the
    task to an internal client either passed to it during instantiation or defaulting
    to the provided implementation
    """

    __client: HttpClient
    __token: str

    def __init__(self, token: str, client: Optional[HttpClient] = None) -> None:
        """
        :param token: The authorization token used for API authentication.
        :type token: str
        :param client: An optional :class:`HttpClient` instance for making requests.
            If not provided, a default :class:`RequestClient` instance will be used.
        :type client: Optional[:class:`HttpClient`], optional
        """
        self.__token = token
        if client is not None:
            self.__client = client
        else:
            self.__client = RequestClient()

    def post(
        self,
        endpoint: str,
        parameters: Dict[str, Union[int, float, str]],
        files: Optional[Dict[str, bytes]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Tuple[int, bytes]:
        """
        Perform an authenticated HTTP POST request to the Imagine API.

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
        final_headers = {"Bearer": self.__token}
        if headers is not None:
            final_headers = {**final_headers, **headers}
            
        return self.__client.post(
            endpoint=endpoint, parameters=parameters, files=files, headers=final_headers
        )
