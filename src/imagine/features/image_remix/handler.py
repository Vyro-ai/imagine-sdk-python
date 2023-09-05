from typing import Optional
from ...remote.http_client import HttpClient
from ...models.response import Response
from ...models.image import Image
from ...utils.error.checker import check_and_raise
from ...utils.file.read import read_image_file_as_bytes
from ...utils.parameter.checker import parameter_builder, non_optional_parameter_checker


class ImageRemixHandler:
    """
    The ImageRemixHandler class is responsible for remixing images based on
    specified parameters using the Imagine API's image remixing endpoint.

    This class facilitates the interaction with the Imagine API to remix
    images by providing an image to be remixed, a prompt, a style ID, and
    control parameters for the remixing process.
    """

    __client: HttpClient
    __endpoint: str = "/edits/remix"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(
        self,
        image_path: str,
        prompt: str,
        style_id: int,
        control: str,
        *,
        seed: Optional[int] = None,
        strength: Optional[int] = None,
        steps: Optional[int] = None,
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
            control=control,
            seed=seed,
            strength=strength,
            steps=steps,
            cfg=cfg,
            negative_prompt=neg_prompt,
        )

        files = {"image": read_image_file_as_bytes(image_path)}

        status_code, content = self.__client.post(self.__endpoint, parameters, files)

        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
