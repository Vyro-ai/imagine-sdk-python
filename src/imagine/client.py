from typing import Optional
from ._handlers.image.alter_image import AlterImageHandler
from ._handlers.image.generations import GenerationsHandler
from ._handlers.image.image_remix import ImageRemixHandler
from ._handlers.image.in_painting import InPaintHandler
from ._handlers.image.super_resolution import SuperResolutionHandler
from ._handlers.image.variate import VariateHandler
from .enums.alter_image.style_ids import AlterImageStyle
from .enums.generations.style_ids import GenerationsStyle
from .enums.image_remix.controls import RemixControls
from .enums.image_remix.style_ids import ImageRemixStyle
from .enums.in_painting.model_versions import InPaintingModel
from .enums.super_resolution.model_versions import SuperResoultionStyle
from .models.image.response import ResponseImage
from .models.imagine.response import Response
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
        :param client: An optional instance of :class:HttpClient to use for requests.
        :type client: Optional[:class:HttpClient]
        """
        self.__token = token
        self.__client = RestClient(token, client)

    def generations(
        self,
        prompt: str,
        *,
        style: GenerationsStyle = GenerationsStyle.STYLE_IMAGINE_V1,
        aspect_ratio: Optional[str] = None,
        neg_prompt: Optional[str] = None,
        cfg: Optional[float] = None,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        high_res_results: Optional[int] = None,
    ) -> Response[ResponseImage]:
        """
        Generate an image based on specified parameters using the
        GenerationsHandler.

        :param prompt: The prompt for generating the image.
        :type prompt: str
        :param style: The style for the image generation (default:
            GenerationsStyle.STYLE_IMAGINE_V1).
        :type style: :class:GenerationsStyle
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
        :param high_res_results: The level of high-resolution results (default: None).
        :type high_res_results: Optional[int]
        :return: A response containing the generated error or an :class:ResponseImage
            object.
        :rtype: :class:Response[:class:ResponseImage]
        """
        handler = GenerationsHandler(self.__client)

        return handler(
            prompt=prompt,
            style_id=style.value,
            aspect_ratio=aspect_ratio,
            cfg=cfg,
            seed=seed,
            neg_prompt=neg_prompt,
            high_res_results=high_res_results,
            steps=steps,
        )

    def image_remix(
        self,
        image_path: str,
        prompt: str,
        *,
        style: ImageRemixStyle = ImageRemixStyle.STYLE_IMAGINE_V1,
        control: RemixControls = RemixControls.OPENPOSE,
        seed: Optional[int] = None,
        strength: Optional[int] = None,
        steps: Optional[int] = None,
        cfg: Optional[float] = None,
        neg_prompt: Optional[str] = None,
    ) -> Response[ResponseImage]:
        """
        Remix an image based on specified parameters using the
        ImageRemixHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param prompt: The prompt for remixing the image.
        :type prompt: str
        :param style: The style for the image remixing (default:
            ImageRemixStyle.STYLE_IMAGINE_V1).
        :type style: :class:ImageRemixStyle
        :param control: The control settings for remixing (default:
            RemixControls.OPENPOSE).
        :type control: :class:RemixControls
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
        :return: A response containing the generated error or an :class:ResponseImage
            object.
        :rtype: :class:Response[:class:ResponseImage]
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
        m_ver: SuperResoultionStyle = SuperResoultionStyle.MODEL_VERSION_1,
    ) -> Response[ResponseImage]:
        """
        Enhance the resolution of an image using the SuperResolutionHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param m_ver: The model version for super resolution.
        :type m_ver: :class:SuperResoultionStyle
        :return: A response containing the generated error or an :class:ResponseImage
            object.
        :rtype: :class:Response[:class:ResponseImage]
        """
        handler = SuperResolutionHandler(self.__client)

        return handler(image_path=image_path, model_version=m_ver.value)

    def variate(
        self,
        image_path: str,
        prompt: str,
        *,
        style: GenerationsStyle = GenerationsStyle.STYLE_IMAGINE_V1,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        strength: Optional[int] = None,
        cfg: Optional[float] = None,
        neg_prompt: Optional[str] = None,
    ) -> Response[ResponseImage]:
        """
        Generate a variation of an image based on specified parameters using
        the VariateHandler. It is an extension of generations hence why it
        uses the same enums as Generations.

        :param image_path: The path to the source image.
        :type image_path: str
        :param prompt: The prompt for generating the variation.
        :type prompt: str
        :param style: The style for generating the variation.
        :type style: :class:GenerationsStyle
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
        :return: A response containing the generated error or an :class:ResponseImage
            object.
        :rtype: :class:Response[:class:ResponseImage]
        """
        handler = VariateHandler(self.__client)

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
        model_version: InPaintingModel = InPaintingModel.MODEL_VERSION_1,
    ) -> Response[ResponseImage]:
        """
        Perform image in-painting based on specified parameters using the
        InPaintHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param mask_path: The path to the mask image for in-painting.
        :type mask_path: str
        :param prompt: The prompt for guiding the in-painting process.
        :type prompt: str
        :param model_version: The model version for in-painting.
        :type model_version: :class:InPaintingModel
        :return: A response containing the generated error or an :class:ResponseImage
            object.
        :rtype: :class:Response[:class:ResponseImage]
        """
        handler = InPaintHandler(self.__client)

        return handler(
            prompt=prompt,
            image_path=image_path,
            mask_path=mask_path,
            model_version=model_version.value,
        )

    def alter_image(
        self,
        image_path: str,
        prompt: str,
        *,
        style: AlterImageStyle = AlterImageStyle.STYLE_ID_1,
        neg_prompt: Optional[str] = None,
        aspect_ratio: Optional[str] = None,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        generation_bias: Optional[float] = None,
        artistic_noise: Optional[float] = None,
        aesthetic_weight: Optional[float] = None,
    ) -> Response[ResponseImage]:
        """
        Alter an image based on specified parameters using the
        AlterImageHandler.

        :param image_path: The path to the source image.
        :type image_path: str
        :param prompt: The prompt for image alteration.
        :type prompt: str
        :param style: The style ID for image alteration.
        :type style: :class:AlterImageStyle
        :param neg_prompt: The negative prompt for generating contrasting alterations.
        :type neg_prompt: Optional[str]
        :param aspect_ratio: The aspect ratio of the altered image.
        :type aspect_ratio: Optional[str]
        :param seed: The random seed for reproducible alteration.
        :type seed: Optional[int]
        :param steps: The number of steps for altering the image.
        :type steps: Optional[int]
        :param generation_bias: The bias for image generation.
        :type generation_bias: Optional[float]
        :param artistic_noise: The amount of artistic noise to apply.
        :type artistic_noise: Optional[float]
        :param aesthetic_weight: The weight of aesthetic changes.
        :type aesthetic_weight: Optional[float]
        :return: A response containing the generated error or an :class:ResponseImage
            object.
        :rtype: :class:Response[:class:ResponseImage]
        """
        handler = AlterImageHandler(self.__client)

        return handler(
            prompt=prompt,
            image_path=image_path,
            style_id=style.value,
            neg_prompt=neg_prompt,
            aspect_ratio=aspect_ratio,
            seed=seed,
            steps=steps,
            generation_bias=generation_bias,
            artistic_noise=artistic_noise,
            aesthetic_weight=aesthetic_weight,
        )
