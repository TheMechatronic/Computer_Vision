import cv2    
import numpy as np
from tkinter import Tk
from tkinter.filedialog import *

def nothing(x):
    pass;

def main():
    Tk().withdraw

    print("ESC key to exit")

    while True:
        # Load the image
        frame = cv2.imread('Object_Detection\Images\Smarties_1_bad_lighting.jpg')

        # Convert the image to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Set the Red Filter Values:
        # Lower Bounds
        l_v = 175
        l_h = 165
        l_s = 0
        # Upper Bounds
        u_v = 179
        u_h = 255
        u_s = 255

        # Define the bounds for the color space filter:
        l_mask_brown = np.array([l_v, l_h, l_s])
        u_mask_brown = np.array([u_v, u_h, u_s])

        # Set the Brown Filter Values:
        # Lower Bounds
        l_v = 0
        l_h = 118
        l_s = 49
        # Upper Bounds
        u_v = 17
        u_h = 165
        u_s = 184

        # Define the bounds for the color space filter:
        l_mask_red = np.array([l_v, l_h, l_s])
        u_mask_red = np.array([u_v, u_h, u_s])

        # Define the mask:
        mask_red = cv2.inRange(hsv, l_mask_red, u_mask_red)
        mask_brown = cv2.inRange(hsv, l_mask_brown, u_mask_brown)
        mask = cv2.bitwise_or(mask_brown, mask_red)

        # Get the result after the mask is applied:
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Show the results of the masking:
        cv2.imshow("frame", frame)
        cv2.imshow("mask_1", mask_red)
        cv2.imshow("mask_2", mask_brown)
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