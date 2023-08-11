def read_image_file_as_bytes(image_path: str) -> bytes:
    """
    Read the content of an image file and return it as bytes.

    :param image_path: The path to the image file.
    :type image_path: str
    :return: The content of the image file as bytes.
    :rtype: bytes
    
    Usage:
    >>> image_path = "path/to/your/image.jpg"
    >>> image_data = read_image_file_as_bytes(image_path)
    >>> print(f"Image data as bytes: {image_data[:10]}... (truncated)")
    """
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    return image_bytes
