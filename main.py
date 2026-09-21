import numpy as np
from PIL import Image
from filters import grayscale

image = Image.open("input/popper.png")

img = np.array(image)

print(img.shape)
print(img.dtype)
print(img[0,0])


gray = gray.astype(np.uint8)

grey_image = Image.fromarray(gray)

grey_image.save("output/export.png")

print("Grayscale image saved...")
