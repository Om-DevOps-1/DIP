'''
NAME: OM ALOK MISHRA
DATE: 8/9/2024
TO CONVERT COLORFUL IMAGE TO GRAYSCALE IMAGE
'''

import cv2
import numpy as np

# Load the color image
image_path = './treeRGB.png'
color_image = cv2.imread(image_path)

# Check if the image was loaded successfully
if color_image is None:
    print(f"Error: Image not found at path {image_path}")
    exit()

# Split the BGR image into its component channels
blue_channel, green_channel, red_channel = cv2.split(color_image)

# Compute the grayscale image as the average of the R, G, B channels
gray_image_manual = (blue_channel.astype(np.float32) + green_channel.astype(np.float32) + red_channel.astype(np.float32)) / 3
gray_image_manual = np.round(gray_image_manual).astype(np.uint8)  # Round and convert to uint8

# Save the grayscale image
output_path = 'path/to/save/grayscale_image.jpg'
cv2.imwrite(output_path, gray_image_manual)

# Optionally, display the images
cv2.imshow('Color Image', color_image)
cv2.imshow('Grayscale Image', gray_image_manual)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
