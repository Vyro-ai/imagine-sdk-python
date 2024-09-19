from typing import Optional
from ....remote.http_client import HttpClient
from ....models.response import Response
from ....models.image import Image

from ....enums import Styles, Controls

from .remix.handler import RemixHandler


class Remix:
    """
    The Remix class is responsible for interacting with input images to
    edit them based on selected methods and their provided configs.

    """

    __client: HttpClient

    __remix_handler: RemixHandler

    def __init__(self, client: HttpClient):
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

        self.__remix_handler = RemixHandler(self.__client)

    def remix(
        self,
        image_path: str,
        prompt: str,
        *,
        style: Styles.Remix = Styles.Remix.IMAGINE_V1,
        control: Controls.Remix = Controls.Remix.OPENPOSE,
        seed: Optional[int] = None,
        strength: Optional[int] = None,
        steps: Optional[int] = None,
        cfg: Optional[float] = None,
        neg_prompt: Optional[str] = None,
    ) -> Response[Image]:
        """
        Remix an image based on specified parameters using the
        ImageRemixHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param prompt: The prompt for remixing the image.
        :type prompt: str
        :param style: The style for the image remixing (default:
            ImageRemixStyle.STYLE_IMAGINE_V1).
        :type style: :class:`ImageRemixStyle`
        :param control: The control settings for remixing (default:
            RemixControls.OPENPOSE).
        :type control: :class:`RemixControls`
        :param seed: The random seed for reproducible remixing (default: None).
        :type seed: Optional[int]
        :param strength: The strength of the remixing effect (default: None).
        :type strength: Optional[int]
        :param steps: The number of steps for remixing the image (default: None).
        :type steps: Optional[int]
        :param cfg: The cfg parameter for remixing (default: None).
        :type cfg: Optional[float]
        :param neg_prompt: The negative prompt for remixing (default: None).
        :type neg_prompt: Optional[str]
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__remix_handler(
            prompt=prompt,
            image_path=image_path,
            style_id=style.value,
            control=control.value,
            seed=seed,
            strength=strength,
            steps=steps,
            cfg=cfg,
            neg_prompt=neg_prompt,
        )
