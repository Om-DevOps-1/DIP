# Histogram Equalization

This repository contains a Python implementation of histogram equalization for image processing using OpenCV and NumPy.

## Overview

The code provides functionality to:
- Load an image and convert it to grayscale if necessary.
- Perform histogram equalization to enhance the contrast of the image.
- Save and display the original and equalized images.

## How It Works

1. **Image Loading**: The `main` function loads the image from a specified path.
2. **Grayscale Conversion**: The image is converted to grayscale if it is in color.
3. **Histogram Calculation**: The histogram of the grayscale image is computed.
4. **Cumulative Distribution Function (CDF)**: The CDF is calculated and normalized.
5. **Pixel Mapping**: The original grayscale image pixels are mapped to equalized values based on the normalized CDF.

## Example

### Main Function
The main function reads an image and applies histogram equalization:

```python
# Load the image
image_path = './treeRGB.png'
image = cv2.imread(image_path)
