import heapq
from collections import Counter, defaultdict

# Node class for the Huffman Tree
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(image):
    # Flatten the 3x3 image to a single list of pixel values
    flat_image = [pixel for row in image for pixel in row]
    # Count the frequency of each pixel value
    frequency = Counter(flat_image)
    return frequency

def build_huffman_tree(frequency):
    # Create a priority queue of nodes
    priority_queue = [Node(symbol, freq) for symbol, freq in frequency.items()]
    heapq.heapify(priority_queue)
    
    # Build the Huffman Tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]  # The root of the Huffman Tree

def generate_huffman_codes(root):
    codes = {}
    
    def generate_codes(node, current_code=""):
        if node is not None:
            if node.symbol is not None:
                codes[node.symbol] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")
    
    generate_codes(root)
    return codes

def huffman_encode(image, codes):
    # Flatten the image
    flat_image = [pixel for row in image for pixel in row]
    encoded_image = ''.join(codes[pixel] for pixel in flat_image)
    return encoded_image

def huffman_coding(image):
    # Calculate frequencies
    frequency = calculate_frequencies(image)
    
    # Build Huffman Tree
    root = build_huffman_tree(frequency)
    
    # Generate Huffman codes
    codes = generate_huffman_codes(root)
    
    # Encode the image
    encoded_image = huffman_encode(image, codes)
    
    return codes, encoded_image

# Example 3x3 image with 3-bit pixel values
image = [
    [0, 1, 2],
    [1, 3, 4],
    [2, 5, 6]
]

# Perform Huffman coding
codes, encoded_image = huffman_coding(image)

print("Huffman Codes:")
for symbol, code in codes.items():
    print(f"Pixel Value: {symbol}, Code: {code}")

print(f"Encoded Image: {encoded_image}")
