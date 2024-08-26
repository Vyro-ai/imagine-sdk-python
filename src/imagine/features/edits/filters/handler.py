from typing import Optional
from ....remote.http_client import HttpClient
from ....models.response import Response
from ....models.image import Image
from ....utils.file.read import read_image_file_as_bytes
from ....utils.error.checker import check_and_raise
from ....utils.parameter.checker import (
    non_optional_parameter_checker,
    parameter_builder,
)
from ....constants import DEFAULT_FILTER_ID, DEFAULT_STYLE_ID
from ....enums import Filters


def ids(id):
    if not id:
        return {
            "filterId": DEFAULT_FILTER_ID,
            "styleId": DEFAULT_STYLE_ID,
        }

    base_value = 1000
    filter_id = id % base_value
    style_id = id // base_value
    return {
        "filterId": filter_id,
        "styleId": style_id,
    }


class FiltersHandler:
    """
    The FiltersHandler class is responsible for applying different art
    style filters to a provided image.

    """

    __client: HttpClient
    __endpoint: str = "/edits/filters"

    def __init__(self, client: HttpClient) -> None:
        """
        :param client: An instance of an HTTP client used to make requests to the API.
        :type client: :class:`HttpClient`
        """
        self.__client = client

    def __call__(self, image_path: str, filter_id: Filters) -> Response[Image]:
        # Validate that image_path is valid
        error: Optional[ValueError] = non_optional_parameter_checker(
            image_path=image_path, filter_id=filter_id
        )
        check_and_raise(error)

        filter_id, style_id = ids(filter_id)

        parameters = parameter_builder(filter_id=filter_id, style_id=style_id)
        files = {"image": read_image_file_as_bytes(image_path)}
        status_code, content = self.__client.post(self.__endpoint, files, parameters)
        if status_code != 200:
            return Response(None, status_code)

        result = Image(content)

        return Response(result, status_code)
