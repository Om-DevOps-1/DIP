# Shannon-Fano Coding Implementation

This repository contains a Python implementation of Shannon-Fano coding, a method of entropy encoding used for lossless data compression.

## Overview

The code includes functions to:
- Calculate the frequency of pixel values in a 3x3 image.
- Generate Shannon-Fano codes for the pixel values based on their frequencies.

## How It Works

1. **Frequency Calculation**: The `calculate_frequency` function flattens a 3x3 image into a single list of pixel values and counts the frequency of each value using the `Counter` from the `collections` module.
   
2. **Shannon-Fano Coding**: The `shannon_fano_coding` function generates binary codes for each unique pixel value based on their frequencies, using a recursive approach.

## Example

The code includes an example 3x3 image with pixel values:
```python
image = [
    [0, 1, 2],
    [1, 3, 4],
    [2, 5, 6]
]
