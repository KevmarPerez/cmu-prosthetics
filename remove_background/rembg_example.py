from rembg.bg import remove
import numpy as np
import cv2
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

input_image = '.\\image1.jpg'
output_image = 'output-image.png'
output_image_pil = '.\\pil-output.png'
output_image_num = 'num-output.png'

# input and output as bytes
def as_bytes():
    with open(input_image, 'rb') as i:
        with open(output_image, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)

def as_pil():
    image = Image.open(input_image, mode='r')
    input_file = Image.open(input_image)
    background = Image.new('RGBA', (image.width,image.height), (255, 255, 255, 255))
    output = remove(input_file)
    background.save(output_image_pil)

def as_numArry():
    input_file = cv2.imread(input_image)
    output = remove(input_file)
    cv2.imwrite(output_image_num, output)

as_pil()