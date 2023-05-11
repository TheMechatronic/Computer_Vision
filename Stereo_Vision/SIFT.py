import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the images
img1 = cv2.imread('Stereo_Vision\Images\Smarties_Book_left.jpg', 0)  # queryImage
img2 = cv2.imread('Stereo_Vision\Images\Smarties_Book_right.jpg', 0)  # trainImage

# Check if the images have different sizes
if img1.shape != img2.shape:
   # Resize the images to a common size
   width = min(img1.shape[1], img2.shape[1])
   height = min(img1.shape[0], img2.shape[0])
   img1 = cv2.resize(img1, (width, height))
   img2 = cv2.resize(img2, (width, height))

# Step 2: Detect and compute SIFT features
sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Step 3: Match the features using FLANN
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Store all the good matches as per Lowe's ratio test.
good = []
for m, n in matches:
    if m.distance < 0.5 * n.distance:
        good.append(m)

# Step 4: Compute the disparity (difference in x-coordinates) for the matched points
if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # Calculate disparity (x-coordinates difference)
    disparity = np.abs(src_pts[:, :, 0] - dst_pts[:, :, 0])

    print('Disparity:', disparity)

    # Draw matches
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Display the result
    plt.imshow(img3), plt.show()

else:
    print('Not enough matches are found - %d/%d' % (len(good), 10))
