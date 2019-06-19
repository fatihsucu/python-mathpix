
bulk_image_response = {
  "reply": {
    "batch_id": "11"
  },
  "result": {
    "algebra": {
      "detection_list": [],
      "detection_map": {
        "contains_chart": 0,
        "contains_diagram": 0,
        "contains_geometry": 0,
        "contains_graph": 0,
        "contains_table": 0,
        "is_inverted": 0,
        "is_not_math": 0,
        "is_printed": 0
      },
      "error": "",
      "latex": "12 + 5 x - 8 = 12 x - 10",
      "latex_confidence": 0.99640350138238,
      "latex_list": [],
      "position": {
        "height": 208,
        "top_left_x": 0,
        "top_left_y": 0,
        "width": 1380
      }
    },
    "inverted": {
      "detection_list": [
        "is_inverted",
        "is_printed"
      ],
      "detection_map": {
        "contains_chart": 0,
        "contains_diagram": 0,
        "contains_geometry": 0,
        "contains_graph": 0,
        "contains_table": 0,
        "is_inverted": 1,
        "is_not_math": 0,
        "is_printed": 1
      },
      "error": "",
      "latex": "x ^ { 2 } + y ^ { 2 } = 9",
      "latex_confidence": 0.99982263230866,
      "latex_list": [],
      "position": {
        "height": 170,
        "top_left_x": 48,
        "top_left_y": 85,
        "width": 544
      }
    }
  }
}

callback_data = {
    "method": "post",
    "url": "https://www.someurl.com",
    "sessionId": "some_id"
}

position_data = {
   "height": 215,
   "top_left_x": 57,
   "top_left_y": 0,
   "width": 605
}

detection_map = {
    "contains_chart": 0,
     "contains_diagram": 0,
     "contains_geometry": 0,
     "contains_graph": 0,
     "contains_table": 0,
     "is_inverted": 0,
     "is_not_math": 0,
     "is_printed": 1
}

ocr_data = {
    "detection_list": [],
    "detection_map": {
        "contains_chart": 0,
        "contains_diagram": 0,
        "contains_geometry": 0,
        "contains_graph": 0,
        "contains_table": 0,
        "is_inverted": 0,
        "is_not_math": 0,
        "is_printed": 0
    },
    "error": "",
    "latex": "\\lim _ { x \\rightarrow 3 } ( \\frac { x ^ { 2 } + 9 } { x - 3 } )",
    "latex_confidence": 0.86757309488734,
    "position": {
        "height": 273,
        "top_left_x": 57,
        "top_left_y": 14,
        "width": 605
    }
}

json_syntax = {
    "error_info": {
            "id": "json_syntax",
            "message": "error_message"
    }
}

image_missing = {
    "error_info": {
            "id": "image_missing",
            "message": "error_message"
    }
}

image_download_error = {
    "error_info": {
            "id": "image_download_error",
            "message": "error_message"
    }
}

image_decode_error = {
    "error_info": {
            "id": "image_decode_error",
            "message": "error_message"
    }
}

image_no_content = {
    "error_info": {
            "id": "image_no_content",
            "message": "error_message"
    }
}


image_not_supported = {
    "error_info": {
            "id": "image_not_supported",
            "message": "error_message"
    }
}


image_max_size = {
    "error_info": {
            "id": "image_max_size",
            "message": "error_message"
    }
}


opts_bad_callback = {
    "error_info": {
            "id": "opts_bad_callback",
            "message": "error_message"
    }
}


opts_unknown_ocr = {
    "error_info": {
            "id": "opts_unknown_ocr",
            "message": "error_message"
    }
}


opts_unknown_format = {
    "error_info": {
            "id": "opts_unknown_format",
            "message": "error_message"
    }
}


math_confidence = {
    "error_info": {
            "id": "math_confidence",
            "message": "error_message"
    }
}


math_syntax = {
    "error_info": {
            "id": "math_syntax",
            "message": "error_message"
    }
}


batch_unknown_id = {
    "error_info": {
            "id": "batch_unknown_id",
            "message": "error_message"
    }
}


sys_exception = {
    "error_info": {
            "id": "sys_exception",
            "message": "error_message"
    }
}