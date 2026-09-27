# PixelOPS

A simple CLI image processing tool built with Python, NumPy, and Pillow.

## Features

* Grayscale
* Sepia
* Brightness adjustment
* Contrast adjustment
* Image inversion
* NumPy-based pixel manipulation
* Image loading and saving

## How It Works

Images are represented as NumPy arrays:

```text
RGB  → (height, width, 3)
RGBA → (height, width, 4)
```

The channels represent Red, Green, Blue, and optionally Alpha.

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

Adds or subtracts a value from pixel intensities and keeps them within the `0–255` range.

### Contrast

Adjusts pixel values around the midpoint `128`:

```text
new_pixel = factor × (pixel - 128) + 128
```

### Invert

Inverts RGB values:

```text
new_pixel = 255 - pixel
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

* Blur
* Edge detection
* Image resizing
* Cropping
* Sharpening
* Histogram processing
* More filters
