from typing import Optional
from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image
from ...enums import AspectRatio, Styles
from .generations.handler import GenerationsHandler
from .variations.handler import VariationsHandler
from .background.handler import BackgroundHandler


class Generations:
    """
    The Generations class is responsible for generating images through
    vairous methods that further use Imagine API's generation enpoints.
    """

    __client: HttpClient

    __generations_handler: GenerationsHandler
    __variations_handler: VariationsHandler
    __background_handler: BackgroundHandler

    def __init__(self, client: HttpClient):
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

        self.__generations_handler = GenerationsHandler(self.__client)
        self.__variations_handler = VariationsHandler(self.__client)
        self.__background_handler = BackgroundHandler(self.__client)

    def generations(
        self,
        prompt: str,
        *,
        style: Styles.Generations = Styles.Generations.IMAGINE_V1,
        aspect_ratio: AspectRatio = AspectRatio.ONE_RATIO_ONE,
        neg_prompt: Optional[str] = None,
        cfg: Optional[float] = None,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        high_res_results: bool = False,
    ) -> Response[Image]:
        """
        Generate an image based on specified parameters using the
        Generations.

        :param prompt: The prompt for generating the image.
        :type prompt: str
        :param style: The style for the image generation (default:
            GenerationsStyle.STYLE_IMAGINE_V1).
        :type style: :class:`GenerationsStyle`
        :param aspect_ratio: The aspect ratio of the image (default: None).
        :type aspect_ratio: Optional[str]
        :param neg_prompt: The negative prompt for contrasting images (default: None).
        :type neg_prompt: Optional[str]
        :param cfg: The cfg parameter for image generation (default: None).
        :type cfg: Optional[float]
        :param seed: The random seed for reproducible generation (default: None).
        :type seed: Optional[int]
        :param steps: The number of steps for generating the image (default: None).
        :type steps: Optional[int]
        :param high_res_results: The level of high-resolution results (default: False).
        :type high_res_results: bool
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__generations_handler(
            prompt=prompt,
            style_id=style.value,
            aspect_ratio=aspect_ratio.value,
            cfg=cfg,
            seed=seed,
            neg_prompt=neg_prompt,
            high_res_results=int(high_res_results),
            steps=steps,
        )

    def variations(
        self,
        image_path: str,
        prompt: str,
        *,
        style: Styles.Variations = Styles.Variations.IMAGINE_V1,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        strength: Optional[int] = None,
        cfg: Optional[float] = None,
        neg_prompt: Optional[str] = None,
    ) -> Response[Image]:
        """
        Generate a variation of an image based on specified parameters using
        the VariationsHandler. It is an extension of generations hence why it
        uses the same styles as Generations.

        :param image_path: The path to the source image.
        :type image_path: str
        :param prompt: The prompt for generating the variation.
        :type prompt: str
        :param style: The style for generating the variation.
        :type style: :class:`GenerationsStyle`
        :param seed: The random seed for reproducible generation.
        :type seed: Optional[int]
        :param steps: The number of steps for generating the variation.
        :type steps: Optional[int]
        :param strength: The strength of the variation effect.
        :type strength: Optional[int]
        :param cfg: The cfg parameter for generating the variation.
        :type cfg: Optional[float]
        :param neg_prompt: The negative prompt for contrasting variations.
        :type neg_prompt: Optional[str]
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__variations_handler(
            prompt=prompt,
            image_path=image_path,
            style_id=style.value,
            strength=strength,
            seed=seed,
            steps=steps,
            cfg=cfg,
            neg_prompt=neg_prompt,
        )

    def background(
        self,
        image_path: str,
        prompt: str,
    ) -> Response[Image]:
        """
        Generate a background of an image based on a prompt.

        :param image_path: The path to the source image.
        :type image_path: str
        :param prompt: The prompt for generating the variation.
        :type prompt: str
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        return self.__background_handler(
            prompt=prompt,
            image_path=image_path,
        )
