from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image
from .remover.handler import RemoverHandler


class Background:
    """
    The Background class is responsible for interacting with the
    backgrounds of images.

    """

    __client: HttpClient

    __remover_handler: RemoverHandler

    def __init__(self, client: HttpClient):
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

        self.__remover_handler = RemoverHandler(self.__client)

    def remover(
        self,
        image_path: str,
    ) -> Response[Image]:
        """
        Remove the background of an image

        :param image_path: The path to the source image.
        :type image_path: str
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__remover_handler(
            image_path=image_path,
        )
