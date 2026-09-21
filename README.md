# PixelOPS

A simple CLI image processing tool built with Python, NumPy, and Pillow.

## Features

* RGB to grayscale conversion
* NumPy-based pixel manipulation
* Image loading and saving

## How It Works

RGB images are represented as NumPy arrays:

```text
(height, width, 3)
```

where the three channels represent Red, Green, and Blue.

Grayscale conversion uses:

```text
Gray = 0.299R + 0.587G + 0.114B
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
