from typing import Optional
from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image
from ...utils.error.checker import check_and_raise
from ...utils.file.read import read_image_file_as_bytes
from ...utils.parameter.checker import parameter_builder, non_optional_parameter_checker


class SuperResolutionHandler:
    """
    The SuperResolutionHandler class is responsible for performing image
    super-resolution using the Imagine API's image upscaling endpoint.

    This class facilitates the interaction with the Imagine API to upscale
    images using super-resolution techniques, providing the image to be
    upscaled and the model version to be used.
    """

    __client: HttpClient
    __endpoint: str = "/upscale/"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(self, image_path: str, model_version: str) -> Response[Image]:
        # Validate prompt and image_path
        error: Optional[ValueError] = non_optional_parameter_checker(
            image_path=image_path
        )
        check_and_raise(error)

        parameters = parameter_builder(model_version=model_version)

        files = {"image": read_image_file_as_bytes(image_path)}

        status_code, content = self.__client.post(self.__endpoint, parameters, files)
        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
