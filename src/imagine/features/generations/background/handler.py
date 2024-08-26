from typing import Optional
from remote.http_client import HttpClient
from models.response import Response
from models.image import Image

from utils.error.checker import check_and_raise
from utils.parameter.checker import parameter_builder, non_optional_parameter_checker
from utils.file.read import read_image_file_as_bytes


class BackgroundHandler:
    """
    The BackgroundHandler class is responsible for generating a background of an input image

    This class facilitates the interaction with the Imagine API to generate
    images by providing a prompt, and an image.
    """

    __client: HttpClient
    __endpoint: str = "/generations/background"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(self, prompt: str, image_path: str) -> Response[Image]:
        # Validate that prompt is not empty
        error: Optional[ValueError] = non_optional_parameter_checker(prompt=prompt)
        check_and_raise(error)

        files = {"image": read_image_file_as_bytes(image_path)}

        parameters = parameter_builder(
            prompt=prompt,
        )

        status_code, content = self.__client.post(
            self.__endpoint, parameters, files=files
        )
        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
