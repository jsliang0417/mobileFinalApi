from lib2to3.pytree import convert
import numpy as np
from PIL import Image, ImageOps
import base64
import io


def Dog_Image_Preprocessing(reversed_code):
    convert = base64.b64decode(reversed_code)
    image = io.BytesIO(convert)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image).convert('RGB')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    return data