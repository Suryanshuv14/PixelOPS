import numpy as np
from PIL import Image
from filters import grayscale, sepia, brightness, invert, contrast


image = Image.open("input/popper.png")

img = np.array(image)

# prinht(img.shape)
# print(img.dtype)
# print(img[0, 0])
print("Choose any One:")
print("Sepia - 1")
print("Grayscale - 2")
print("Brightness - 3")
print("Invert - 4")
print("Contrast - 5")

choice = input()

if choice == "1":

    sepia_img = sepia(img)

    sepia_image = Image.fromarray(sepia_img)
    sepia_image.save("output/export.png")

elif choice == "2":

    gray = grayscale(img)

    grey_image = Image.fromarray(gray)
    grey_image.save("output/export.png")

elif choice == "3":
    value = int(input("Enter brightness value: "))

    bright = brightness(img, value)

    bright_image = Image.fromarray(bright)
    bright_image.save("output/export.png")

elif choice == "4":

    invert_img = invert(img)

    invert_image = Image.fromarray(invert_img)
    invert_image.save("output/export.png")

elif choice == "5":
    factor = float(input("Enter factor for contrsat : "))

    contrast_img = contrast(img, factor)
    contrast_image = Image.fromarray(contrast_img)
    contrast_image.save("output/export.png")
else:
    print("Invalid choice")

print("Image saved...")