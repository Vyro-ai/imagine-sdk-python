from typing import Optional
from ....remote.http_client import HttpClient
from ....models.response import Response
from ....models.image import Image
from ....utils.error.checker import check_and_raise
from ....utils.file.read import read_image_file_as_bytes
from ....utils.parameter.checker import parameter_builder, non_optional_parameter_checker


class VariationsHandler:
    """
    The VariateHandler class is responsible for generating image variations
    based on specified parameters using the Imagine API's image variations
    endpoint.

    This class facilitates the interaction with the Imagine API to generate
    image variations by providing a prompt, the base image to be varied, a
    style ID, and various optional parameters for control.
    """

    __client: HttpClient
    __endpoint: str = "/generations/variations"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(
        self,
        prompt: str,
        image_path: str,
        style_id: int,
        *,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        strength: Optional[int] = None,
        cfg: Optional[float] = None,
        neg_prompt: Optional[str] = None,
    ) -> Response[Image]:
        # Validate prompt and image_path
        error: Optional[ValueError] = non_optional_parameter_checker(
            prompt=prompt, image_path=image_path
        )
        check_and_raise(error)

        parameters = parameter_builder(
            prompt=prompt,
            style_id=style_id,
            cfg=cfg,
            seed=seed,
            strength=strength,
            steps=steps,
            negative_prompt=neg_prompt,
        )

        files = {"image": read_image_file_as_bytes(image_path)}

        status_code, content = self.__client.post(
            self.__endpoint, parameters=parameters, files=files
        )
        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
