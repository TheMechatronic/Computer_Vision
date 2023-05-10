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

        # Set the Red Filter Values:
        # Lower Bounds
        l_r = 167
        l_g = 38
        l_b = 52
        # Upper Bounds
        u_r = 255
        u_g = 71
        u_b = 80

        # Define the bounds for the color space filter:
        l_mask_brown = np.array([l_b, l_g, l_r])
        u_mask_brown = np.array([u_b, u_g, u_r])

        # Set the Brown Filter Values:
        # Lower Bounds
        l_r = 113
        l_g = 75
        l_b = 33
        # Upper Bounds
        u_r = 173
        u_g = 114
        u_b = 66

        # Define the bounds for the color space filter:
        l_mask_red = np.array([l_b, l_g, l_r])
        u_mask_red = np.array([u_b, u_g, u_r])

        # Define the mask:
        mask_red = cv2.inRange(frame, l_mask_red, u_mask_red)
        mask_brown = cv2.inRange(frame, l_mask_brown, u_mask_brown)
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