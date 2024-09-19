from typing import Optional

from .features.generations.handler import Generations
from .features.background.handler import Background
from .features.edits.handler import Edits
from .features.enhance.handler import Enhance
from .features.face.handler import Face

from .remote.http_client import HttpClient
from .remote.rest.http_client import RestClient


class Imagine:
    """
    The main interaction class for the Imagine SDK.

    This class provides methods for interacting with various image generation
    and manipulation functions.
    """

    __client: HttpClient

    __generations_handler: Generations
    __background_handler: Background
    __edits_handler: Edits
    __enhance_handler: Enhance
    __face_handler: Face

    def __init__(self, token: str, *, client: Optional[HttpClient] = None) -> None:
        """
        Initialize an instance of the Imagine class.

        :param token: The authorization token used for API authentication.
        :type token: str
        :param client: An optional instance of :class:`HttpClient` to use for requests.
        :type client: Optional[:py:class:`HttpClient`]
        """
        self.__client = RestClient(token, client)

        self.__generations_handler = Generations(self.__client)
        self.__background_handler = Background(self.__client)
        self.__edits_handler = Edits(self.__client)
        self.__enhance_handler = Enhance(self.__client)
        self.__face_handler = Face(self.__client)

    @property
    def generations(self) -> Generations:
        """
        Instances of all the methods that do generations

        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`

        :return: An instance of the Generations handler.
        :rtype: class:Generations
        """
        return self.__generations_handler

    @property
    def background(self) -> Background:
        """
        Instances of all the methods to interact with the background of an image

        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`

        :return: An instance of the Background handler.
        :rtype: class:Background
        """
        return self.__background_handler

    @property
    def edits(self) -> Edits:
        """
        Instances of all the methods to edit an image

        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`

        :return: An instance of the Edits handler.
        :rtype: class:Edits
        """
        return self.__edits_handler

    @property
    def enhance(self) -> Enhance:
        """
        Instances of all the methods to enhance an image

        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`

        :return: An instance of the Enhance handler.
        :rtype: class:Enhance
        """
        return self.__enhance_handler

    @property
    def face(self) -> Face:
        """
        Instances of all the methods to edit a subject's image while maintaining facial identity

        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`

        :return: An instance of the Face handler.
        :rtype: class:Face
        """
        return self.__face_handler
