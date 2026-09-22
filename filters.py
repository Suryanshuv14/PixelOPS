import numpy as np

def grayscale(img):
    gray = (
        0.299 * img[:, :, 0] +
        0.587 * img[:, :, 1] +
        0.114 * img[:, :, 2]
    )

    return gray.astype(np.uint8)

def sepia(img):
    R = img[:,:,0] 
    G = img[:,:,1] 
    B = img[:,:,2] 

    sepia_r = 0.393 * R + 0.769 * G + 0.189 * B
    sepia_g = 0.349 * R + 0.686 * G + 0.168 * B
    sepia_b = 0.272 * R + 0.534 * G + 0.131 * B

    result = np.stack([sepia_r, sepia_g, sepia_b], axis=2)



    return np.clip(result,0,255).astype(np.uint8)