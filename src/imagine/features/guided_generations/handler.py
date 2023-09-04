from typing import Optional
from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image
from ...utils.error.checker import check_and_raise
from ...utils.file.read import read_image_file_as_bytes
from ...utils.parameter.checker import parameter_builder, non_optional_parameter_checker


class GuidedGenerationsHandler:
    """
    The AlterImageHandler class is responsible for altering images based on
    specified parameters using the Imagine API's guided image generation
    endpoint.

    This class facilitates the interaction with the Imagine API to generate
    altered images by providing various parameters like prompts, style IDs,
    and more.
    """

    __client: HttpClient
    __endpoint: str = "/generations/guided"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:HttpClient
        """
        self.__client = client

    def __call__(
        self,
        prompt: str,
        image_path: str,
        style_id: int,
        *,
        neg_prompt: Optional[str] = None,
        aspect_ratio: Optional[str] = None,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        generation_bias: Optional[float] = None,
        artistic_noise: Optional[float] = None,
        aesthetic_weight: Optional[float] = None,
    ) -> Response[Image]:
        # Validate prompt and image_path
        error: Optional[ValueError] = non_optional_parameter_checker(
            prompt=prompt, image_path=image_path
        )
        check_and_raise(error)

        parameters = parameter_builder(
            prompt=prompt,
            style_id=style_id,
            negative_prompt=neg_prompt,
            aspect_ratio=aspect_ratio,
            seed=seed,
            steps=steps,
            generation_bias=generation_bias,
            artistic_noise=artistic_noise,
            aesthetic_weight=aesthetic_weight,
        )

        files = {"image": read_image_file_as_bytes(image_path)}

        status_code, content = self.__client.post(self.__endpoint, parameters, files)
        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
