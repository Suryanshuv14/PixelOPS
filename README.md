# PixelOPS

A simple CLI image processing tool built with Python, NumPy, and Pillow.

## Features

* RGB to grayscale and Sepia conversion
* Brightness adjustment
* Image inversion
* NumPy-based pixel manipulation
* Image loading and saving

## How It Works

RGB images are represented as NumPy arrays:

```text
(height, width, 3)
```

where the three channels represent Red, Green, and Blue.

RGBA images contain an additional Alpha channel:

```text
(height, width, 4)
```

### Grayscale

```text
Gray = 0.299R + 0.587G + 0.114B
```

### Sepia

```text
sepia_r = 0.393R + 0.769G + 0.189B
sepia_g = 0.349R + 0.686G + 0.168B
sepia_b = 0.272R + 0.534G + 0.131B
```

### Brightness

A value is added to each pixel and limited to the valid `0-255` range.

### Invert

```text
New Pixel = 255 - Old Pixel
```

## Setup

```bash
git clone https://github.com/your-username/PixelOPS.git
cd PixelOPS

python -m venv .venv
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Place input images in `input/`. Processed images are saved to `output/`.

## Tech Stack

* Python
* NumPy
* Pillow

## Planned

* Contrast
* Blur
* Edge detection
* Image resizing
* Cropping
* More filters
