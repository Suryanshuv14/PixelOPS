import numpy as np
from PIL import Image
from filters import grayscale, sepia


image = Image.open("input/popper.png")

img = np.array(image)

# print(img.shape)
# print(img.dtype)
# print(img[0, 0])

print("Choose any One:")
print("Sepia - 1")
print("Grayscale - 2")

choice = input()

if choice == "1":

    sepia_img = sepia(img)

    sepia_image = Image.fromarray(sepia_img)
    sepia_image.save("output/export.png")

elif choice == "2":

    gray = grayscale(img)

    grey_image = Image.fromarray(gray)
    grey_image.save("output/export.png")

else:
    print("Invalid choice")

print("Image saved...")