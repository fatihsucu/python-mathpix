import requests
import json
from .errors import *


class Client(object):

    def __init__(self, app_id=None, app_key=None):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = "https://api.mathpix.com/v3/latex"

    def __handle_exception(self, error_data):
        error_id = error_data.get('id')
        error_message = error_data.get('message')
        if error_id == "json_syntax":
            raise JSONSyntaxException(message=error_message)
        elif error_id == "image_missing":
            raise ImageMissingException(message=error_message)
        elif error_id == "image_download_error":
            raise ImageDownloadException(message=error_message)
        elif error_id == "image_decode_error":
            raise ImageDecodeException(message=error_message)
        elif error_id == "image_no_content":
            raise ImageNoContentException(message=error_message)
        elif error_id == "image_not_supported":
            raise ImageNotSupportedException(message=error_message)
        elif error_id == "image_max_size":
            raise ImageMaxSizeException(message=error_message)
        elif error_id == "opts_bad_callback":
            raise BadCallbackException(message=error_message)
        elif error_id == "opts_unknown_ocr":
            raise UnknownOcrException(message=error_message)
        elif error_id == "opts_unknown_format":
            raise UnknownFormatException(message=error_message)
        elif error_id == "math_confidence":
            raise MathConfidenceException(message=error_message)
        elif error_id == "math_syntax":
            raise MathSyntaxException(message=error_message)
        elif error_id == "batch_unknown_id":
            raise UnknownBatchIdException(message=error_message)
        elif error_id == "sys_exception":
            raise SysException(message=error_message)

    def post(self, data):
        response = requests.post(
            self.base_url,
            data=json.dumps(data),
            headers={
                "app_id": self.app_id,
                "app_key": self.app_key,
                "Content-Type": "application/json"
            }
        )

        if response.status_code == 401:
            raise UnauthorizedException("Unauthorized request received. Check your credentials.")
        elif response.status_code == 429:
            raise MaxRequestsException("Max Request limit exceeded.")

        elif "error_info" in response.json():
            self.__handle_exception(response.json()['error_info'])

        return response.json()

    def get(self, *args, **kwargs):
        raise NotImplementedError()

    def put(self, *args, **kwargs):
        raise NotImplementedError()
