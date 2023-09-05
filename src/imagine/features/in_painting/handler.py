from typing import Optional
from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image
from ...utils.error.checker import check_and_raise
from ...utils.file.read import read_image_file_as_bytes
from ...utils.parameter.checker import parameter_builder, non_optional_parameter_checker


class InPaintHandler:
    """
    The InPaintHandler class is responsible for inpainting images using the
    Imagine API's image inpainting endpoint.

    This class facilitates the interaction with the Imagine API to perform
    image inpainting operations by providing a prompt, the image to be
    inpainted, a mask indicating the areas to be filled, and the model
    version to be used.
    """

    __client: HttpClient
    __endpoint: str = "/edits/inpaint"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(
        self, prompt: str, image_path: str, mask_path: str, model_version: str
    ) -> Response[Image]:
        # Validate prompt and image_path
        error: Optional[ValueError] = non_optional_parameter_checker(
            prompt=prompt, image_path=image_path, mask_path=mask_path
        )
        check_and_raise(error)

        parameters = parameter_builder(prompt=prompt, model_version=model_version)

        files = {
            "image": read_image_file_as_bytes(image_path),
            "mask": read_image_file_as_bytes(mask_path),
        }

        status_code, content = self.__client.post(self.__endpoint, parameters, files)

        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
