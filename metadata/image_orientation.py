import os, base64
from PIL import Image, ImageFile
from PIL.ExifTags import TAGS
from rembg.bg import remove
import io
import exif

img_folder = './temp'
image_filename = './image1.jpg'

def save_meta():
    img = exif.Image(image_filename)
    # img_ls = sorted(img.list_all())
    # meta = img.get_all()
    return img.get_all()

def modify_meta(image, meta_data):
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    byte_im = buf.getvalue()
    img = exif.Image(byte_im)
    print(meta_data)

    for attr, val in meta_data.items():
        # print(f'{attr}:{val}')
        try:
            img.set(attr, val)
        except:
            print(f'{attr}:{val}')
            pass
    print(img.get_all())
    return img



def as_pil(image, n=0):
    """ Function to remove background images and save the output in temp folder """
    meta = exif.Image(image_filename).get_all()
    input_file = Image.open(image_filename)
    output = remove(input_file).convert('RGB')
    # output.save(os.path.join(input_nobg, f'image{n}.jpg'))
    mod_img = modify_meta(output, meta)
    print(type(mod_img))
    # mod_img.save(os.path.join(input_nobg, f'image{n}.jpg'))

# print(Image.open(image_filename).getexif())
as_pil(image_filename)
# print(save_meta())
# imgs = os.listdir(img_folder)

# with open(image_filename, 'rb') as img_file:
#     img = Image(image_filename)

# for attr in img.list_all():
#     print(f'{attr}:{img.get(attr)}')

# orientation = img.get("orientation")
# print(f'Before: {orientation}')
# img.orientation = 2

# with open('new_image.png', 'wb') as new_image:
#     new_image.write(img.get_file())
# print(f'After: {orientation}')