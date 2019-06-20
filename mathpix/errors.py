
class BaseException(Exception):

    def __init__(self, message):
        self.message = message


class UnauthorizedException(BaseException):
    pass


class MaxRequestsException(BaseException):
    pass


class JSONSyntaxException(BaseException):
    pass


class ImageMissingException(BaseException):
    pass


class ImageDownloadException(BaseException):
    pass


class ImageDecodeException(BaseException):
    pass


class ImageNoContentException(BaseException):
    pass


class ImageNotSupportedException(BaseException):
    pass


class ImageMaxSizeException(BaseException):
    pass


class BadCallbackException(BaseException):
    pass


class UnknownOcrException(BaseException):
    pass


class UnknownFormatException(BaseException):
    pass


class MathConfidenceException(BaseException):
    pass


class MathSyntaxException(BaseException):
    pass


class UnknownBatchIdException(BaseException):
    pass


class SysException(BaseException):
    pass


class InvalidCallbackException(BaseException):
    pass


class InvalidUrlException(BaseException):
    pass
