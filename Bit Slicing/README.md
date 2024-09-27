# Bit Slicing of 3-Bit Images

This repository contains a Python implementation for creating and visualizing bit planes from a synthetic 3-bit image.

## Overview

The code provides functions to:
- Create a synthetic 3-bit image with random pixel values.
- Extract and visualize the bit planes of the image.

## How It Works

1. **Image Creation**: The `create_3bit_image` function generates a random 3-bit image where each pixel value is between 0 and 7.

2. **Bit Slicing**: The `bit_slicing` function extracts each bit plane from the image.

3. **Displaying Bit Planes**: The `display_bit_planes` function visualizes the extracted bit planes using Matplotlib.

## Example

### Main Function
The main function creates an 8x8 synthetic 3-bit image and slices it into bit planes:

```python
width, height = 8, 8  # Image dimensions
image = create_3bit_image(width, height)
print("Original 3-bit Image:")
print(image)
