from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image

from .upsacle.handler import UpscaleHandler


class Enhance:
    """
    The Enhance class is responsible for enhancing images.

    """

    __client: HttpClient

    __upscale_handler: UpscaleHandler

    def __init__(self, client: HttpClient):
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

        self.__upscale_handler = UpscaleHandler(self.__client)

    def upscale(
        self,
        image_path: str,
    ) -> Response[Image]:
        """
        Enhance the resolution of an image using the UpscaleHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__upscale_handler(image_path=image_path)
