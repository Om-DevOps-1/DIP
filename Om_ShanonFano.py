from collections import Counter

def calculate_frequency(image):
    # Flatten the 3x3 image to a single list of pixel values
    flat_image = [pixel for row in image for pixel in row]
    # Count the frequency of each pixel value
    frequency = Counter(flat_image)
    return frequency

def shannon_fano_coding(frequency):
    # Sort symbols by frequency in descending order
    sorted_symbols = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Recursive function to generate codes
    def encode(symbols):
        if len(symbols) == 1:
            # Base case: single symbol
            return {symbols[0][0]: ""}
        
        total = sum(freq for _, freq in symbols)
        cumulative = 0
        split_index = 0
        
        for i, (_, freq) in enumerate(symbols):
            cumulative += freq
            if cumulative >= total / 2:
                split_index = i
                break
        
        left = symbols[:split_index + 1]
        right = symbols[split_index + 1:]
        
        left_codes = encode(left)
        right_codes = encode(right)
        
        codes = {}
        codes.update({symbol: "0" + code for symbol, code in left_codes.items()})
        codes.update({symbol: "1" + code for symbol, code in right_codes.items()})
        
        return codes
    
    return encode(sorted_symbols)

# Example 3x3 image with 3-bit pixel values
image = [
    [0, 1, 2],
    [1, 3, 4],
    [2, 5, 6]
]

# Calculate frequencies
frequency = calculate_frequency(image)
print("Frequency of pixel values:", frequency)

# Apply Shannon-Fano coding
shannon_fano_codes = shannon_fano_coding(frequency)
print("Shannon-Fano Codes:")
for symbol, code in shannon_fano_codes.items():
    print(f"Pixel Value: {symbol}, Code: {code}")
