# Arithmetic Coding Implementation

This repository contains a Python implementation of arithmetic coding, a form of entropy encoding used in lossless data compression.

## Overview

The code provides functions to:
- Calculate the frequency and probability of symbols in a given message.
- Compute cumulative intervals for each symbol based on their probabilities.
- Encode a message into a single floating-point value using arithmetic coding.

## How It Works

1. **Frequency Calculation**: The function `calculate_frequencies` counts the occurrences of each symbol and computes their probabilities.
2. **Interval Calculation**: The function `calculate_intervals` determines the cumulative intervals for each symbol based on calculated probabilities.
3. **Arithmetic Encoding**: The function `arithmetic_encode` encodes the message using the intervals.

## Example

The code includes an example message `"abacabad"`. When you run the script, it performs arithmetic coding and prints the symbol intervals.

### Example Output
```plaintext
Symbol Intervals:
a: (0.0, 0.5)
b: (0.5, 0.75)
c: (0.75, 0.875)
d: (0.875, 1.0)
