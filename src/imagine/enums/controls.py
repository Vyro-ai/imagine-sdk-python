from enum import Enum


class Controls:
    class Remix(Enum):
        """
        Enums for image_remix to guide image generation
        """

        OPENPOSE = "openpose"
        SCRIBBLE = "scribble"
        CANNY = "canny"
        LINEART = "lineart"
        DEPTH = "depth"
