from typing import Any, Dict
from ...type.multipart import MultipartForm, MultipartFile


def multipart_form_builder(params: Dict[str, Any]) -> MultipartForm:
    """
    Build a dictionary of MultipartForm items from the given parameters.

    This utility function constructs a dictionary by iterating through the
    key-value pairs in the provided keyword arguments and creating MultipartForm
    items for each parameter. Each MultipartForm item consists of a parameter's
    key, a None value (as a placeholder for file data), and the parameter's value
    converted to a string.

    :param params: Keyword arguments with keys as strings and values of any type.
    :type params: Dict[str, Any]
    :return: A dictionary containing MultipartForm items.
    :rtype: Dict[str, Tuple[None, str]]

    Usage:
        >>> data_params = {"name": "John", "age": 30, "city": "New York"}
        >>> multipart_data = multipart_builder(data_params)
        >>> print(multipart_data)
        {'name': (None, 'John'), 'age': (None, '30'), 'city': (None, 'New York')}
    """
    return {k: (None, str(v)) for (k, v) in params.items()}


def multipart_file_builder(
    params: Dict[str, Any], *, extension: str = "jpeg", content_type: str = "image/jpeg"
) -> MultipartFile:
    """
    Build a dictionary of MultipartFile tuples for each parameter.

    This function constructs a dictionary by iterating through the provided
    parameters' key-value pairs and creating MultipartFile tuples for each
    parameter. The MultipartFile tuple consists of the parameter's value
    along with a suggested filename and content type for an image file.

    :param params: The parameters for which MultipartFile (Three-Tuple format:
        ('file_name', file_bytes, 'content_type')) tuples need to be created.
    :type params: Dict[str, Any]
    :param extension: The file extension to be used in the filename.
    :type extension: str, optional
    :param content_type: The content type of the file.
    :type content_type: str, optional
    :return: A dictionary containing MultipartFile tuples for each parameter.
    :rtype: Dict[str, Tuple[str, Any, str]]

    Usage:
        >>> image_params = {
        ...     "image1": image_bytes_data,
        ...     "image2": image_bytes_data,
        ... }
        ...
        >>> image_files = multipart_file_builder(image_params, extension=".jpg",
            content_type="image/jpeg")
        >>> print(image_files)
        {'image1.jpg': image_bytes_data, 'image2.jpg': image_bytes_data}
    """
    return {k: (f"{k}.{extension}", v, content_type) for (k, v) in params.items()}
