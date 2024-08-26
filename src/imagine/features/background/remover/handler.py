from typing import Optional
from ....remote.http_client import HttpClient
from ....models.response import Response
from ....models.image import Image
from ....utils.file.read import read_image_file_as_bytes
from ....utils.error.checker import check_and_raise
from ....utils.parameter.checker import non_optional_parameter_checker


class RemoverHandler:
    """
    The RemoverHandler class is responsible for removing the background of and image
    using the Imagine API's background removal endpoint.

    """

    __client: HttpClient
    __endpoint: str = "/background/remover"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(
        self,
        image_path: str,
    ) -> Response[Image]:
        # Validate that image_path is valid
        error: Optional[ValueError] = non_optional_parameter_checker(
            image_path=image_path
        )
        check_and_raise(error)
        files = {"image": read_image_file_as_bytes(image_path)}

        status_code, content = self.__client.post(self.__endpoint, files=files)
        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
