import cv2
import numpy as np

def update_disparity_map(block_size, num_disparities):
    # Ensure the number of disparities is divisible by 16
    if num_disparities % 16 != 0:
        num_disparities = (num_disparities // 16) * 16

    # Create a StereoBM object for disparity calculation
    stereo = cv2.StereoBM_create(numDisparities=num_disparities, blockSize=block_size)

    # Compute the disparity map
    disparity_map = stereo.compute(left_image, right_image)

    # Normalize the disparity map for better visualization
    disparity_map_normalized = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Display the disparity map with updated parameters
    cv2.imshow('result', disparity_map_normalized)
    cv2.imshow('image', right_image)

def on_block_size_change(value):
    block_size = 2 * value + 5
    update_disparity_map(block_size, num_disparities)

def on_num_disparities_change(value):
    num_disparities = 16 * value
    update_disparity_map(block_size, num_disparities)

# Load the left and right stereo images
left_image = cv2.imread('Stereo_Vision\Images\Smarties_left.jpg', 0)  # Read grayscale image
right_image = cv2.imread('Stereo_Vision\Images\Smarties_right.jpg', 0)  # Read grayscale image

# Check if the images have different sizes
if left_image.shape != right_image.shape:
    # Resize the images to a common size
    width = min(left_image.shape[1], right_image.shape[1])
    height = min(left_image.shape[0], right_image.shape[0])
    left_image = cv2.resize(left_image, (width, height))
    right_image = cv2.resize(right_image, (width, height))

# Set the initial values for block size and number of disparities
initial_block_size = 5
initial_num_disparities = 4

# Initialize the block size and number of disparities
block_size = 2 * initial_block_size + 5
num_disparities = 16 * initial_num_disparities

# Create a window for displaying the disparity map
cv2.namedWindow('Disparity Map')

# Create trackbars for adjusting the block size and number of disparities
cv2.createTrackbar('Block Size', 'Disparity Map', initial_block_size, 25, on_block_size_change)
cv2.createTrackbar('Num Disparities', 'Disparity Map', initial_num_disparities, 20, on_num_disparities_change)

# Initially compute and display the disparity map
update_disparity_map(block_size, num_disparities)

# Wait for the ESC key to be pressed
while cv2.waitKey(1) != 27:
    pass

cv2.destroyAllWindows()
