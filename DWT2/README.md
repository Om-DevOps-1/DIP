# Wavelet Transform of Images

This project demonstrates the use of wavelet transforms on images using Python libraries, specifically `PyWavelets` and `Matplotlib`. The code performs a discrete wavelet transform (DWT) on a sample image and visualizes the results.

## Prerequisites

Make sure you have the following Python libraries installed:

- `numpy`
- `matplotlib`
- `pywt`

You can install the required libraries using pip:

```bash
pip install numpy matplotlib PyWavelets
```

## Usage

- Load the image: The code uses the built-in camera image from PyWavelets as the input.
- Perform DWT: The image is transformed using the Discrete Wavelet Transform (DWT).
- Visualize results: The approximation and detail coefficients (horizontal, vertical, and diagonal) are plotted.


## Output

The output of this code is a figure displaying four subplots:

- Approximation: The low-frequency components of the image.
- Horizontal detail: The horizontal edges detected in the image.
- Vertical detail: The vertical edges detected in the image.
- Diagonal detail: The diagonal edges detected in the image
