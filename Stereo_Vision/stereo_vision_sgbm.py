import cv2
import numpy as np

def update_disparity_map(left_image, right_image):
    # Retrieve the values from the sliders
    block_size = cv2.getTrackbarPos('Block Size', 'Disparity Map')
    block_size = 2 * block_size + 5
    num_disparities = cv2.getTrackbarPos('Num Disparities', 'Disparity Map') * 16
    p1 = cv2.getTrackbarPos('P1', 'Disparity Map')
    p2 = cv2.getTrackbarPos('P2', 'Disparity Map')
    uniqueness_ratio = cv2.getTrackbarPos('Uniqueness Ratio', 'Disparity Map')
    speckle_window_size = cv2.getTrackbarPos('Speckle Window Size', 'Disparity Map')
    speckle_range = cv2.getTrackbarPos('Speckle Range', 'Disparity Map')

    # Create a StereoSGBM object for disparity calculation
    stereo = cv2.StereoSGBM_create(
        minDisparity=0,
        numDisparities=num_disparities,
        blockSize=block_size,
        P1=p1,
        P2=p2,
        disp12MaxDiff=-1,
        preFilterCap=0,
        uniquenessRatio=uniqueness_ratio,
        speckleWindowSize=speckle_window_size,
        speckleRange=speckle_range
    )

    # Compute the disparity map
    disparity_map = stereo.compute(left_image, right_image)

    # Normalize the disparity map for better visualization
    disparity_map_normalized = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Display the disparity map with updated parameters
    cv2.imshow('image', right_image)
    cv2.imshow('Result', disparity_map_normalized)

def main():
    # Load the left and right stereo images
    left_image = cv2.imread('Stereo_Vision\Images\Smarties_Book_left.jpg', 0)  # Read grayscale image
    right_image = cv2.imread('Stereo_Vision\Images\Smarties_Book_right.jpg', 0)  # Read grayscale image

    # Check if the images have different sizes
    if left_image.shape != right_image.shape:
        # Resize the images to a common size
        width = min(left_image.shape[1], right_image.shape[1])
        height = min(left_image.shape[0], right_image.shape[0])
        left_image = cv2.resize(left_image, (width, height))
        right_image = cv2.resize(right_image, (width, height))

    # Set the initial values for the parameters
    initial_block_size = 5
    initial_num_disparities = 4
    initial_p1 = 8
    initial_p2 = 32
    initial_uniqueness_ratio = 10
    initial_speckle_window_size = 100
    initial_speckle_range = 32

    # Create a window for displaying the disparity map
    cv2.namedWindow('Disparity Map')

    # Create sliders for adjusting the parameters
    cv2.createTrackbar('Block Size', 'Disparity Map', initial_block_size, 25, lambda x: update_disparity_map(left_image, right_image))
    cv2.createTrackbar('Num Disparities', 'Disparity Map', initial_num_disparities, 20, lambda x: update_disparity_map(left_image, right_image))
    cv2.createTrackbar('P1', 'Disparity Map', initial_p1, 100, lambda x: update_disparity_map(left_image, right_image))
    cv2.createTrackbar('P2', 'Disparity Map', initial_p2, 100, lambda x: update_disparity_map(left_image, right_image))
    cv2.createTrackbar('Uniqueness Ratio', 'Disparity Map', initial_uniqueness_ratio, 50, lambda x: update_disparity_map(left_image, right_image))
    cv2.createTrackbar('Speckle Window Size', 'Disparity Map', initial_speckle_window_size, 200, lambda x: update_disparity_map(left_image, right_image))
    cv2.createTrackbar('Speckle Range', 'Disparity Map', initial_speckle_range, 50, lambda x: update_disparity_map(left_image, right_image))

    # Initially compute and display the disparity map
    update_disparity_map(left_image, right_image)

    while True:
        # Wait for the ESC key to be pressed
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

