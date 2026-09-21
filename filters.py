import numpy as np

def grayscale(img):
    gray = (
        0.299 * img[:, :, 0] +
        0.587 * img[:, :, 1] +
        0.114 * img[:, :, 2]
    )

    return gray.astype(np.uint8)