from exif import Image

img_filename = "image1.jpg"

img = Image(img_filename)

# print(img.has_exif)
img_ls = sorted(img.list_all())

for val in img_ls:
    print(f"{val} : {img.get(val)}")