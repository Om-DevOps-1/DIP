# Color to Black-and-White Image Converter

This repository contains a Python script that converts a colorful image to a black-and-white (grayscale) image using OpenCV.

## Overview

The script performs the following functions:
- Reads a color image from a specified path.
- Converts the image to grayscale.
- Saves and displays the resulting black-and-white image.

## Example

### Code

The script reads an image from the specified path, converts it, and displays the result:

```python
import cv2

# Read the color image
image_path = './treeRGB.png'
color_image = cv2.imread(image_path)

# Convert the image to grayscale
bw_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Save the black and white image
cv2.imwrite("black_and_white_image.jpg", bw_image)

cv2.imshow("Black and White Image", bw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
