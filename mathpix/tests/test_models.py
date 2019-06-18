import unittest
from .dataset import ocr_data, position_data, detection_map
from mathpix.mathpix import Ocr, Position, DetectionMap


class OcrTest(unittest.TestCase):

    def test_ocr_load_and_json(self):
        ocr = Ocr.load(ocr_data)
        assert isinstance(ocr, Ocr)
        assert isinstance(ocr.detection_map, DetectionMap)
        assert isinstance(ocr.position, Position)
        self.assertEqual(ocr.latex, ocr_data['latex'])
        self.assertEqual(ocr.latex_confidence, ocr_data['latex_confidence'])
        self.assertEqual(ocr.detection_map.is_inverted, ocr_data['detection_map']['is_inverted'])

        self.assertEqual(ocr.__json__().keys(), ocr_data.keys())

    def test_position_load_and_json(self):
        position = Position.load(position_data)
        assert isinstance(position, Position)
        self.assertEqual(position.width, position_data['width'])
        self.assertEqual(position.top_left_y, position_data['top_left_y'])
        self.assertEqual(position.top_left_x, position_data['top_left_x'])
        self.assertEqual(position.height, position_data['height'])
        self.assertEqual(position.__json__().keys(), position_data.keys())

    def test_determination_map_load_and_json(self):
        detection_map_ins = DetectionMap.load(detection_map)
        assert isinstance(detection_map_ins, DetectionMap)
        self.assertEqual(detection_map_ins.is_inverted, detection_map['is_inverted'])
        self.assertEqual(detection_map_ins.is_printed, detection_map['is_printed'])
        self.assertEqual(detection_map_ins.is_not_math, detection_map['is_not_math'])
        self.assertEqual(detection_map_ins.contains_table, detection_map['contains_table'])
        self.assertEqual(detection_map_ins.contains_graph, detection_map['contains_graph'])
        self.assertEqual(detection_map_ins.contains_geometry, detection_map['contains_geometry'])
        self.assertEqual(detection_map_ins.contains_diagram, detection_map['contains_diagram'])
        self.assertEqual(detection_map_ins.contains_chart, detection_map['contains_chart'])
        self.assertEqual(detection_map_ins.__json__().keys(), detection_map.keys())
