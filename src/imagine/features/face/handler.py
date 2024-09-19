from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image

from .headshot.handler import HeadshotHandler


class Face:
    """
    The Face class is responsible for editing an image while
    maintaining the facial identity of the subject.

    """

    __client: HttpClient

    __headshot_handler: HeadshotHandler

    def __init__(self, client: HttpClient):
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

        self.__headshot_handler = HeadshotHandler(self.__client)

    def headshot(
        self,
        image_path: str,
        prompt: str,
    ) -> Response[Image]:
        """
        Change the clothing of a subject using the HeadshotHandler
        while maintaining facial identity.

        :param image_path: The path to the source image.
        :type image_path: str
        :param prompt: The guidance for editing the image.
        :type prompt: str
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__headshot_handler(image_path=image_path, prompt=prompt)
