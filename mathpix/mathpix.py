from .client import Client
from .utils import encode_image, encode_image_from_url


class Position(object):

    def __init__(self, height, top_left_x, top_left_y, width):
        self.height = height
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width

    @classmethod
    def load(cls, data):
        return Position(
            height=data.get('height'),
            top_left_x=data.get('top_left_x'),
            top_left_y=data.get('top_left_y'),
            width=data.get('width')
        )

    def __json__(self):
        return {
            "height": self.height,
            "top_left_x": self.top_left_x,
            "top_left_y": self.top_left_y,
            "width": self.width
        }


class DetectionMap(object):

    def __init__(
            self, contains_chart, contains_diagram,
            contains_geometry, contains_graph, contains_table,
            is_inverted, is_not_math, is_printed
    ):
        self.contains_chart = contains_chart
        self.contains_diagram = contains_diagram
        self.contains_geometry = contains_geometry
        self.contains_graph = contains_graph
        self.contains_table = contains_table
        self.is_inverted = is_inverted
        self.is_not_math = is_not_math
        self.is_printed = is_printed

    @classmethod
    def load(cls, data):
        return DetectionMap(
            contains_chart=data.get('contains_chart'),
            contains_diagram=data.get('contains_diagram'),
            contains_graph=data.get('contains_graph'),
            contains_geometry=data.get('contains_geometry'),
            contains_table=data.get('contains_table'),
            is_inverted=data.get('is_inverted'),
            is_not_math=data.get('is_not_math'),
            is_printed=data.get('is_printed')
        )

    def __json__(self):
        return {
            "contains_chart": self.contains_chart,
            "contains_diagram": self.contains_diagram,
            "contains_geometry": self.contains_geometry,
            "contains_graph": self.contains_graph,
            "contains_table": self.contains_table,
            "is_inverted": self.is_inverted,
            "is_not_math": self.is_not_math,
            "is_printed": self.is_printed
        }


class Ocr(object):

    def __init__(self, detection_list, detection_map, error, latex, latex_confidence, position, reply=None):
        self.reply = reply
        self.detection_list = detection_list
        self.detection_map = detection_map
        self.error = error
        self.latex = latex
        self.latex_confidence = latex_confidence
        self.position = position

    @classmethod
    def load(cls, data):
        if data.get('reply'):
            return Ocr(
                detection_list=data.get('result', {}).get('detection_list'),
                detection_map=DetectionMap.load(data.get('result', {}).get('detection_map')),
                error=data.get('result', {}).get('error'),
                latex=data.get('result', {}).get('latex'),
                latex_confidence=data.get('result', {}).get('latex_confidence'),
                position=Position.load(data.get('result', {}).get('position')),
                reply=data.get('reply')
            )
        return Ocr(
            detection_list=data.get('detection_list'),
            detection_map=DetectionMap.load(data.get('detection_map')),
            error=data.get('error'),
            latex=data.get('latex'),
            latex_confidence=data.get('latex_confidence'),
            position=Position.load(data.get('position')),
            reply=data.get('reply')
        )

    def __json__(self):
        payload = {
            "detection_list": self.detection_list,
            "detection_map": self.detection_map.__json__(),
            "error": self.error,
            "latex": self.latex,
            "latex_confidence": self.latex_confidence,
            "position": self.position.__json__()
        }
        if self.reply:
            return {
                "reply": self.reply,
                "result": payload
            }
        return payload


class MathPix(object):

    def __init__(self, app_id, app_key):
        self.client = Client(app_id=app_id, app_key=app_key)

    def process_image(
            self, image_path=None, image_url=None, region=None,
            ocr=None, skip_recrop=True, confidence_threshold=None,
            confidence_rate_threshold=None, callback=None
    ):
        if image_path:
            encoded = encode_image(image_path)
        elif image_url:
            encoded = encode_image_from_url(image_url)
        else:
            raise Exception("Invalid arguments")

        optionals = {}

        if ocr:
            optionals["ocr"] = ocr

        if not skip_recrop:
            optionals["skip_recrop"] = False

        if confidence_threshold:
            optionals["confidence_threshold"] = confidence_threshold

        if confidence_rate_threshold:
            optionals["confidence_rate_threshold"] = confidence_rate_threshold

        if callback:
            optionals["callback"] = callback

        payload = {
            "src": "data:image/jpeg;base64, {}".format(encoded),
            **optionals
        }
        response = self.client.post(payload)
        return Ocr.load(response)

    def process_image_bulk(self, urls, callback=None):
        ocrs = list()
        payload = {}
        if callback:
            payload["callback"] = callback

        response = self.client.post({**payload, **urls})

        for k, v in response['result'].items():
            ocr = Ocr.load(v)
            ocr.reply = k
            ocrs.append(ocr)

        return ocrs
