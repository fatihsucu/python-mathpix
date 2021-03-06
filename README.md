### Python Mathpix Api Wrapper
This package provides python client for mathpix api. You need to have `app_id`and `app_key` for use this package. You can find more detailed information [https://docs.mathpix.com/](https://docs.mathpix.com/)

#### Installation
##### Command line
```
pip install python-mathpix
```

##### Source code
```
git clone https://github.com/fatihsucu/python-mathpix.git
cd python-mathpix
python setup.py install
```

##### Examples
```
from mathpix.mathpix import MathPix

mathpix = MathPix(app_id="you_app_id", app_key="your_app_key")
```
You can process image with image url.
```
ocr = matphix.process_image(image_url="https://any_image_url.jpg")
```
Or with image path.
```
ocr = mathpix.process_image(image_path="/path/to/perfect/image.jpg")
```
Create a bulk for bulk process
```
from mathpix.mathpix import ImageUrl
urls = [ImageUrl(key="algebria", url="https://image_url"), ImageUrl(key="geometry", url="https://image_url_2")]
ocr = mathpix.process_image_bulk(urls=urls)
```

Defining a callback
```
from mathpix.mathpix import Callback
callback = Callback(method="post", url="https://some_callback_url", sessionId="somesessionId")
```
Validation of callback
```
callback.validate(raise_exception=True) #raise_exception True raises exception
```
After validation of callback you can ask `is_valid()` to callback instance.
```
callback.is_valid()
>>> True
```

```
print(ocr.latex)
>>>'\\left. \\begin{array} { l } { \\quad f ( 2 x ) + f ( \\frac { x } { 3 } ) } \\\\ { \\text { fonksiyonunun periyodu kaçtir? } } \\\\ { \\left. \\begin{array} { l l l l } { \\text { A) } 3 } & { \\text { B) } 6 } & { \\text { C) } 9 } & { \\text { D) } 12 } & { \\text { E) } 1 ! } \\end{array} \\right. } \\end{array} \\right.'

print(ocr.latex_confidence)
>>>0.11452491798799172
```

##### Tests
You can run `nosetests` at the project root.

##### Errors
You can find detailed information about errors at [https://docs.mathpix.com/#errors](https://docs.mathpix.com/#errors)
```
UnauthorizedException  
MaxRequestsException
JSONSyntaxException  
ImageMissingException
ImageDownloadException   
ImageDecodeException
ImageNoContentException
ImageNotSupportedException
ImageMaxSizeException
BadCallbackException
UnknownOcrException
UnknownFormatException
MathConfidenceException
MathSyntaxException
UnknownBatchIdException
SysException 
```
