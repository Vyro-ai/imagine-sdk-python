from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image

from .remix.handler import Remix
from .inpaint.handler import InpaintHandler
from .filters.handler import FiltersHandler

from ...enums import Styles, Filters


class Edits:
    """
    The Edits class is responsible for interacting with input images to
    edit them based on selected methods and their provided configs.

    """

    __client: HttpClient

    __remix_handler: Remix
    __inpaint_handler: InpaintHandler
    __filters_handler: FiltersHandler

    def __init__(self, client: HttpClient):
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

        self.__remix_handler = Remix(self.__client)
        self.__inpaint_handler = InpaintHandler(self.__client)
        self.__filters_handler = FiltersHandler(self.__client)

    @property
    def remix(self) -> Remix:
        """
        Instances of all the methods to edit an image

        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`

        :return: An instance of the Generations handler.
        :rtype: Generations
        """
        return self.__remix_handler

    def inpaint(
        self,
        image_path: str,
        mask_path: str,
        prompt: str,
        *,
        style: Styles.Inpaint = Styles.Inpaint.REALISM,
    ) -> Response[Image]:
        """
        Perform image inpainting based on specified parameters using the
        InpaintHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param mask_path: The path to the mask image for inpainting.
        :type mask_path: str
        :param prompt: The prompt for guiding the inpainting process.
        :type prompt: str
        :param style: The model version for inpainting.
        :type style: :class:`InpaintingModel`
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__inpaint_handler(
            prompt=prompt,
            image_path=image_path,
            mask_path=mask_path,
            style_id=style.value,
        )

    def filters(self, image_path: str, filter: Filters) -> Response[Image]:
        """
        Perform image inpainting based on specified parameters using the
        InpaintHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param filter: The filter id for Filters.
        :type filter: :class:`EditsFilters`
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__filters_handler(image_path=image_path, filter_id=filter)
