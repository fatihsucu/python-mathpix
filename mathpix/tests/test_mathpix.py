import unittest
from unittest.mock import patch
from .dataset import *
from mathpix.mathpix import MathPix, Ocr, Position, DetectionMap, ImageUrl
from mathpix.errors import *


class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class MathPixTest(unittest.TestCase):

    @patch('mathpix.mathpix.Client.post', return_value=ocr_data)
    @patch('mathpix.mathpix.encode_image_from_url')
    def test_process_image(self, mocked_post, encoded_image):
        ocr = MathPix(app_key="test_key", app_id="test_id").process_image(image_url="https://some_awesome_image_url")

        assert isinstance(ocr, Ocr)
        assert isinstance(ocr.position, Position)
        assert isinstance(ocr.detection_map, DetectionMap)
        self.assertEqual(ocr.latex, ocr_data['latex'])
        self.assertEqual(ocr.latex_confidence, ocr_data['latex_confidence'])
        self.assertEqual(ocr.detection_list, ocr_data['detection_list'])

    @patch('mathpix.mathpix.Client.post', return_value=bulk_image_response)
    def test_process_bulk_image(self, mocked_post):
        urls = {
            "inverted": "https://raw.githubusercontent.com/Mathpix/api-examples/master/images/inverted.jpg",
            "algebra": "https://raw.githubusercontent.com/Mathpix/api-examples/master/images/algebra.jpg"
        }

        url_list = [ImageUrl(key=k, url=v) for k, v in urls.items()]
        ocrs = MathPix(app_key="test_key", app_id="test_id").process_image_bulk(urls=url_list)

        assert isinstance(ocrs, list)
        self.assertIn("algebra", [ocr.reply for ocr in ocrs])
        self.assertIn("inverted", [ocr.reply for ocr in ocrs])
        ocr = ocrs[0]
        assert isinstance(ocr, Ocr)
        assert isinstance(ocr.position, Position)
        assert isinstance(ocr.detection_map, DetectionMap)

    @patch('mathpix.mathpix.encode_image_from_url')
    def test_error_handling(self, encoded_image):
        ins = MathPix(app_key="test_key", app_id="test_id")
        with patch('requests.post', return_value=MockResponse(json_data=json_syntax)):
            self.assertRaises(JSONSyntaxException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=image_missing)):
            self.assertRaises(ImageMissingException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=image_download_error)):
            self.assertRaises(ImageDownloadException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=image_decode_error)):
            self.assertRaises(ImageDecodeException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=image_no_content)):
            self.assertRaises(ImageNoContentException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=image_not_supported)):
            self.assertRaises(ImageNotSupportedException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=image_max_size)):
            self.assertRaises(ImageMaxSizeException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=opts_bad_callback)):
            self.assertRaises(BadCallbackException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=opts_unknown_ocr)):
            self.assertRaises(UnknownOcrException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=opts_unknown_format)):
            self.assertRaises(UnknownFormatException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=math_confidence)):
            self.assertRaises(MathConfidenceException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=math_syntax)):
            self.assertRaises(MathSyntaxException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=batch_unknown_id)):
            self.assertRaises(UnknownBatchIdException, ins.process_image, image_url="image_url")

        with patch('requests.post', return_value=MockResponse(json_data=sys_exception)):
            self.assertRaises(SysException, ins.process_image, image_url="image_url")