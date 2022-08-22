import os
from rembg.bg import remove
import numpy as np
import io
from PIL import Image, ImageFile
from tqdm import tqdm

ImageFile.LOAD_TRUNCATED_IMAGES = True

parent_dir = '..\\images\\human'
input_path = os.path.join(parent_dir, 'input')
output_path = os.path.join(parent_dir, 'output')
temp_path = os.path.join(parent_dir, 'temp')
input_nobg = os.path.join(parent_dir, 'input_nobg')

def create_dirs(path):
    # path = os.path.join(parent_dir, n_path)
    try:
        os.makedirs(path)
    except:
        pass

def as_pil(image, n=0):
    """ Function to remove background images and save the output in temp folder """
    input_file = Image.open(os.path.join(input_path, image))
    output = remove(input_file).convert('RGB')
    output.save(os.path.join(input_nobg, f'image{n}.jpg'))

if __name__ == '__main__':
    create_dirs(input_path)
    create_dirs(output_path)
    create_dirs(temp_path)
    create_dirs(input_nobg)
    # get all input images
    imgs = os.listdir(input_path)

    # remove abackground in all images
    for i in tqdm(range(len(imgs))):
        as_pil(imgs[i], i)
        # print(f"Done image {i}")

    