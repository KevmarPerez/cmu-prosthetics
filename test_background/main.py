import os
from rembg.bg import remove
import numpy as np
import io
from PIL import Image, ImageFile
from tqdm import tqdm

ImageFile.LOAD_TRUNCATED_IMAGES = True

parent_dir = '.\\images\\shoe'
input_path = os.path.join(parent_dir, 'input')
output_path = os.path.join(parent_dir, 'output')
temp_path = os.path.join(parent_dir, 'temp')

def create_dirs(path):
    # path = os.path.join(parent_dir, n_path)
    os.makedirs(path)

def as_pil(image, n=0):
    """ Function to remove background images and save the output in temp folder """
    input_file = Image.open(os.path.join(input_path, image)).convert('RGB')
    output = remove(input_file)
    output.save(os.path.join(temp_path, f'image{n}.png'))

if __name__ == '__main__':
    try:
        create_dirs(input_path)
        create_dirs(output_path)
        create_dirs(temp_path)
    except:
        pass

    # get all input images
    imgs = os.listdir(input_path)

    # remove abackground in all images
    for i in tqdm(range(len(imgs))):
        as_pil(imgs[i], i)
        # print(f"Done image {i}")

    