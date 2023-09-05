from enum import Enum


class Status(Enum):
    """
    Enums for Status
    """

    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    UNPROCESSABLE_ENTITY = 422
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503
    MODULE_NOT_FOUND = 1000
    NOT_ENOUGH_TOKENS = 424
