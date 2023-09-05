from typing import Optional
from .features.generations.handler import GenerationsHandler
from .features.image_remix.handler import ImageRemixHandler
from .features.in_painting.handler import InPaintHandler
from .features.super_resolution.handler import SuperResolutionHandler
from .features.generations.variations.handler import VariationsHandler
from .features.generations.style_ids import GenerationsStyle
from .features.image_remix.controls import RemixControls
from .features.image_remix.style_ids import ImageRemixStyle
from .features.in_painting.style_ids import InPaintingStyle
from .features.super_resolution.style_ids import SuperResolutionStyle
from .models.image import Image
from .models.response import Response
from .remote.http_client import HttpClient
from .remote.rest.http_client import RestClient


class Imagine:
    """
    The main interaction class for the Imagine SDK.

    This class provides methods for interacting with various image generation
    and manipulation functions.
    """

    __token: str
    __client: HttpClient

    def __init__(self, token: str, *, client: Optional[HttpClient] = None) -> None:
        """
        Initialize an instance of the Imagine class.

        :param token: The authorization token used for API authentication.
        :type token: str
        :param client: An optional instance of :class:`HttpClient` to use for requests.
        :type client: Optional[:py:class:`HttpClient`]
        """
        self.__token = token
        self.__client = RestClient(token, client)

    def generations(
        self,
        prompt: str,
        *,
        style: GenerationsStyle = GenerationsStyle.IMAGINE_V1,
        aspect_ratio: Optional[str] = None,
        neg_prompt: Optional[str] = None,
        cfg: Optional[float] = None,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        high_res_results: bool = False,
    ) -> Response[Image]:
        """
        Generate an image based on specified parameters using the
        GenerationsHandler.

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
        handler = GenerationsHandler(self.__client)

        return handler(
            prompt=prompt,
            style_id=style.value,
            aspect_ratio=aspect_ratio,
            cfg=cfg,
            seed=seed,
            neg_prompt=neg_prompt,
            high_res_results=int(high_res_results),
            steps=steps,
        )

    def image_remix(
        self,
        image_path: str,
        prompt: str,
        *,
        style: ImageRemixStyle = ImageRemixStyle.IMAGINE_V1,
        control: RemixControls = RemixControls.OPENPOSE,
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
        handler = ImageRemixHandler(self.__client)

        return handler(
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

    def super_resolution(
        self,
        image_path: str,
        *,
        style: SuperResolutionStyle = SuperResolutionStyle.BASIC,
    ) -> Response[Image]:
        """
        Enhance the resolution of an image using the SuperResolutionHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param style: The model version for super resolution.
        :type style: :class:SuperResolutionStyle
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        handler = SuperResolutionHandler(self.__client)

        return handler(image_path=image_path, model_version=style.value)

    def variations(
        self,
        image_path: str,
        prompt: str,
        *,
        style: GenerationsStyle = GenerationsStyle.IMAGINE_V1,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        strength: Optional[int] = None,
        cfg: Optional[float] = None,
        neg_prompt: Optional[str] = None,
    ) -> Response[Image]:
        """
        Generate a variation of an image based on specified parameters using
        the VariateHandler. It is an extension of generations hence why it
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
        handler = VariationsHandler(self.__client)

        return handler(
            prompt=prompt,
            image_path=image_path,
            style_id=style.value,
            strength=strength,
            seed=seed,
            steps=steps,
            cfg=cfg,
            neg_prompt=neg_prompt,
        )

    def in_painting(
        self,
        image_path: str,
        mask_path: str,
        prompt: str,
        *,
        style: InPaintingStyle = InPaintingStyle.BASIC,
    ) -> Response[Image]:
        """
        Perform image in-painting based on specified parameters using the
        InPaintHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param mask_path: The path to the mask image for in-painting.
        :type mask_path: str
        :param prompt: The prompt for guiding the in-painting process.
        :type prompt: str
        :param style: The model version for in-painting.
        :type style: :class:`InPaintingModel`
        :return: A response containing the generated error or an :class:`Image`
            object.
        :rtype: :class:`Response`[:class:`Image`]
        """
        handler = InPaintHandler(self.__client)

        return handler(
            prompt=prompt,
            image_path=image_path,
            mask_path=mask_path,
            model_version=style.value,
        )
