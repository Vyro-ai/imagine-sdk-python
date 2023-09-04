from typing import Optional
from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image
from ...utils.error.checker import check_and_raise
from ...utils.parameter.checker import parameter_builder, non_optional_parameter_checker


class GenerationsHandler:
    """
    The GenerationsHandler class is responsible for generating images based on
    specified parameters using the Imagine API's image generation endpoint.

    This class facilitates the interaction with the Imagine API to generate
    images by providing a prompt, a style ID, and various optional parameters
    for control.
    """

    __client: HttpClient
    __endpoint: str = "/generations"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(
        self,
        prompt: str,
        style_id: int,
        *,
        aspect_ratio: Optional[str] = None,
        neg_prompt: Optional[str] = None,
        cfg: Optional[float] = None,
        seed: Optional[int] = None,
        steps: Optional[int] = None,
        high_res_results: Optional[int] = None,
    ) -> Response[Image]:
        # Validate that prompt is not empty
        error: Optional[ValueError] = non_optional_parameter_checker(prompt=prompt)
        check_and_raise(error)

        parameters = parameter_builder(
            style_id=style_id,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            negative_prompt=neg_prompt,
            cfg=cfg,
            seed=seed,
            steps=steps,
            high_res_results=high_res_results,
        )

        status_code, content = self.__client.post(self.__endpoint, parameters)
        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
