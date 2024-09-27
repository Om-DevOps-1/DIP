# Huffman Coding Implementation

This repository contains a Python implementation of Huffman coding, a popular algorithm for lossless data compression.

## Overview

The code provides functions to:
- Calculate the frequency of pixel values in a 3x3 image.
- Build a Huffman tree based on the frequencies.
- Generate Huffman codes from the tree.
- Encode the image using the generated codes.

## How It Works

1. **Frequency Calculation**: The `calculate_frequencies` function flattens a 3x3 image into a list of pixel values and counts the frequency of each value using `Counter`.

2. **Building the Huffman Tree**: The `build_huffman_tree` function creates a priority queue of nodes and constructs the Huffman tree by merging nodes with the lowest frequencies.

3. **Generating Huffman Codes**: The `generate_huffman_codes` function traverses the Huffman tree to create binary codes for each unique pixel value.

4. **Encoding the Image**: The `huffman_encode` function uses the generated codes to produce a binary string representing the image.

## Example

The code includes an example of a 3x3 image with pixel values:
```python
image = [
    [0, 1, 2],
    [1, 3, 4],
    [2, 5, 6]
]
