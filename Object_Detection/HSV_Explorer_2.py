import cv2    
import numpy as np
from tkinter import Tk
from tkinter.filedialog import *

def nothing(x):
    pass;

def main():
    Tk().withdraw

    # Window to set the trackbars for the first mask:
    cv2.namedWindow("Tracking")
    # Lower bounds trackbars
    cv2.createTrackbar("LH", "Tracking", 0, 179, nothing)
    cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
    # Upper bounds trackbars
    cv2.createTrackbar("UH", "Tracking", 179, 179, nothing)
    cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

    while True:
        # Load the image
        frame_1 = cv2.imread('Object_Detection\Images\Smarties_1_good_lighting.jpg')
        frame_2 = cv2.imread('Object_Detection\Images\Smarties_1_bad_lighting.jpg')

        # Convert the image to hsv
        hsv_1 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2HSV)
        hsv_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2HSV)

        # Get the set trackbar values:
        # Lower Bounds
        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")
        # Upper Bounds
        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")

        # Define the bounds for the color space filter:
        l_mask = np.array([l_h, l_s, l_v])
        u_mask = np.array([u_h, u_s, u_v])

        # Define the mask for the blue:
        mask_1 = cv2.inRange(hsv_1, l_mask, u_mask)
        mask_2 = cv2.inRange(hsv_2, l_mask, u_mask)

        # Get the result after the mask is applied:
        result_1 = cv2.bitwise_and(frame_1, frame_1, mask=mask_1)
        result_2 = cv2.bitwise_and(frame_2, frame_2, mask=mask_2)

        # Show the results of the masking:
        cv2.imshow("frame_1", frame_1)
        cv2.imshow("result_1", result_1)
        cv2.imshow("frame_2", frame_2)
        cv2.imshow("result_2", result_2)

        # Wait for the ESC key and close all windows
        key = cv2.waitKey(1)
        if key == 27:
            break

    return 0

if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()