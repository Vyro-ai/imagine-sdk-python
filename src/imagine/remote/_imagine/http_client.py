from typing import Optional, Dict, Tuple, Union
from ..http_client import HttpClient
from ...type.multipart import Multipart
from ...utils.imports.dynamic import dynamic_import
from ...utils.parameter.multipart import multipart_form_builder, multipart_file_builder


class RequestClient(HttpClient):
    """
    The default provided implementation of :class:HttpClient. RequestClient
    class is responsible for making HTTP POST requests to the Imagine API.
    """

    __base_url: str = "https://api.vyro.ai/v1/imagine/api"

    def post(
        self,
        endpoint: str,
        parameters: Dict[str, Union[int, float, str]],
        files: Optional[Dict[str, bytes]] = None,
        headers: Dict[str, str] = None,
    ) -> Tuple[int, bytes]:
        """
        Perform an HTTP POST request to the Imagine API.

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
        requests = dynamic_import("requests")
        if requests is None:
            return (1000, b"Module requests could not be loaded.")

        url = self.__base_url + endpoint

        multipart: Multipart = multipart_form_builder(parameters)
        if files is not None:
            file_tuple = multipart_file_builder(files)
            multipart = {**multipart, **file_tuple}

        response = requests.post(url, headers=headers, files=multipart, timeout=180)

        return response.status_code, response.content
