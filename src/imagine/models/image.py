from io import BytesIO
from ..utils.imports.dynamic import dynamic_import


class Image:
    """
    A utility class for handling image data as bytes and converting
    it to various formats.

    This class allows you to work with image data represented as bytes
    and provides methods to convert it into a PIL (Pillow) image object
    and a NumPy array.

    :param data: The image data as bytes.
    :type data: bytes
    """

    __data: bytes

    def __init__(self, data: bytes) -> None:
        self.__data = data

    @property
    def bytes(self) -> bytes:
        """
        Get the image data as bytes.

        :return: The image data as bytes.
        :rtype: bytes
        """
        return self.__data

    def to_pil_image(self) -> "PIL.Image.Image":  # noqa: F821
        """
        Convert the image data to a PIL (Pillow) image object.

        :return: A PIL image object.
        :rtype: PIL.Image.Image
        """
        try:
            from PIL import Image

            img = Image.open(BytesIO(self.__data))
            return img
        except ImportError:
            print(
                "Module PIL not found. If you wish to make use of this method,"
                + " consider using pip to install the module in question or providing"
                + " your own implementation."
            )

    def to_numpy(self) -> "numpy.ndarray":  # noqa: F821
        """
        Convert the image data to a NumPy array.

        :return: A NumPy array representing the image.
        :rtype: numpy.ndarray
        """
        np = dynamic_import("numpy")
        if np is None:
            return None

        numpy_array = np.frombuffer(self.__data, dtype=np.uint8)
        return numpy_array

    def as_file(self, file_path: str) -> str:
        """
        Write the image bytes to a file-like object.
        :param file_path: The path of the file to write the image bytes to.
        :type file_path: str
        :return: The file path
        :rtype: str
        """
        with open(file_path, "wb") as file:
            file.write(self.__data)

        return file_path
