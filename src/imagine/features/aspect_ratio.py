from enum import Enum


class AspectRatio(Enum):
    """
    Enums for supported aspect ratios
    """
    ONE_RATIO_ONE = "1:1"
    FOUR_RATIO_THREE = "4:3"
    THREE_RATIO_TWO = "3:2"
    TWO_RATIO_THREE = "2:3"
    SIXTEEN_RATIO_NINE = "16:9"
    NINE_RATIO_SIXTEEN = "9:16"
    FIVE_RATIO_FOUR = "5:4"
    FOUR_RATIO_FIVE = "4:5"
    THREE_RATIO_ONE = "3:1"
    THREE_RATIO_FOUR = "3:4"
