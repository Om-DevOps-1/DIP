import numpy as np
import matplotlib.pyplot as plt

def create_3bit_image(width, height):
    """
    Creates a synthetic 3-bit image with random pixel values.
    Each pixel value is between 0 and 7 (3-bit values).
    """
    return np.random.randint(0, 8, (height, width), dtype=np.uint8)

def bit_slicing(image):
    """
    Bit slices a 3-bit image. Returns a list of images, each representing
    a specific bit plane.
    """
    bit_planes = []
    for bit in range(3):  # 3 bits for a 3-bit image
        bit_plane = (image >> bit) & 1  # Extract bit plane
        bit_planes.append(bit_plane)
    return bit_planes

def display_bit_planes(bit_planes):
    """
    Display bit planes using matplotlib.
    """
    fig, axes = plt.subplots(1, len(bit_planes), figsize=(15, 5))
    for i, bit_plane in enumerate(bit_planes):
        axes[i].imshow(bit_plane, cmap='gray')
        axes[i].set_title(f'Bit Plane {i}')
        axes[i].axis('off')
    plt.show()

# Main function to create and slice a 3-bit image
def main():
    width, height = 8, 8  # Image dimensions
    image = create_3bit_image(width, height)
    print("Original 3-bit Image:")
    print(image)
    
    bit_planes = bit_slicing(image)
    
    print("\nBit Planes:")
    for i, bit_plane in enumerate(bit_planes):
        print(f"Bit Plane {i}:")
        print(bit_plane)
    
    display_bit_planes(bit_planes)

if __name__ == "__main__":
    main()
