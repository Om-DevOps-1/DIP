'''
NAME: OM ALOK MISHRA
DATE: 8/9/2024
TO CONVERT COLORFUL IMAGE TO BLACK-&-WHITE IMAGE
'''
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
