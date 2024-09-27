import cv2
import numpy as np

def histogram_equalization(image):
    # Convert image to grayscale if it's not already
    if len(image.shape) == 3:  # Check if image is in color (not grayscale)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    # Compute the histogram
    hist, bins = np.histogram(gray_image.flatten(), 256, [0, 256])

    # Compute the cumulative distribution function (CDF)
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()  # Normalize the CDF

    # Mask all pixels with zero CDF value
    cdf_m = np.ma.masked_equal(cdf, 0)

    # Normalize the CDF values
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    # Map the original grayscale image pixels to equalized values
    equalized_image = cdf[gray_image]

    return equalized_image

def main():
    # Load the image
    image_path = './treeRGB.png'
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Image not found at path {image_path}")
        return

    # Perform histogram equalization
    equalized_image = histogram_equalization(image)

    # Save and display the results
    output_path = 'path/to/save/equalized_image.jpg'
    cv2.imwrite(output_path, equalized_image)

    # Display the original and equalized images
    cv2.imshow('Original Image', image)
    cv2.imshow('Equalized Image', equalized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
