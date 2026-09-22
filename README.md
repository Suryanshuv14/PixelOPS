# PixelOPS

A simple CLI image processing tool built with Python, NumPy, and Pillow.

## Features

* RGB to grayscale and Sepia conversion
* NumPy-based pixel manipulation
* Image loading and saving

## How It Works

RGB images are represented as NumPy arrays:

```text
(height, width, 3)
```

where the three channels represent Red, Green, and Blue.

Grayscale and Sepia conversion uses:

```text
Gray  : 0.299R + 0.587G + 0.114B
Sepia : 
        sepia_r = 0.393 * R + 0.769 * G + 0.189 * B
        sepia_g = 0.349 * R + 0.686 * G + 0.168 * B
        sepia_b = 0.272 * R + 0.534 * G + 0.131 * B
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

* Brightness
* Contrast
* Blur
* Edge detection
* Image resizing
* More filters
