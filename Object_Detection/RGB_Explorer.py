import cv2    
import numpy as np
from tkinter import Tk
from tkinter.filedialog import *

def nothing(x):
    pass;

def main():
    Tk().withdraw

    # Window to set the trackbars for the mask:
    cv2.namedWindow("Tracking")
    # Lower bounds trackbars
    cv2.createTrackbar("LR", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LG", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LB", "Tracking", 0, 255, nothing)
    # Upper bounds trackbars
    cv2.createTrackbar("UR", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("UG", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("UB", "Tracking", 255, 255, nothing)

    print("ESC key to exit")

    while True:
        # Load the image
        frame = cv2.imread('Object_Detection\Images\Smarties_1_good_lighting.jpg')

        # Get the set trackbar values:
        # Lower Bounds
        l_r = cv2.getTrackbarPos("LR", "Tracking")
        l_g = cv2.getTrackbarPos("LG", "Tracking")
        l_b = cv2.getTrackbarPos("LB", "Tracking")
        # Upper Bounds
        u_r = cv2.getTrackbarPos("UR", "Tracking")
        u_g = cv2.getTrackbarPos("UG", "Tracking")
        u_b = cv2.getTrackbarPos("UB", "Tracking")

        # Define the bounds for the color space filter:
        l_mask = np.array([l_b, l_g, l_r])
        u_mask = np.array([u_b, u_g, u_r])

        # Define the mask for the blue:
        mask = cv2.inRange(frame, l_mask, u_mask)

        # Get the result after the mask is applied:
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Show the results of the masking:
        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)

        # Wait for the ESC key and close all windows
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == 83:
            # saveFilePath  =  asksaveasfilename(initialdir = "/",title = "Mask",filetypes = (("jpeg files","*.jpg"),("all files","*.*")), initialfile = 'mask')
            # cv2.imwrite(saveFilePath, mask)
            saveFilePath  =  asksaveasfilename(initialdir = "/",title = "Result",filetypes = (("jpeg files","*.jpg"),("all files","*.*")), initialfile = 'result')
            cv2.imwrite(saveFilePath, result)
    return 0

if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()