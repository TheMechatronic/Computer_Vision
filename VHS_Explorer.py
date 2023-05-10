import cv2    
import numpy as np

def nothing(x):
    pass;

def main():
    # Window to set the trackbars for the mask:
    cv2.namedWindow("Tracking")
    # Lower bounds trackbars
    cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
    # Upper bounds trackbars
    cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

    print("ESC key to exit")

    while True:
        # Load the image
        frame = cv2.imread('Object_Detection\Images\M_M_good_lighting.jpg')

        # Convert the image to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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
        mask = cv2.inRange(hsv, l_mask, u_mask)

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
    return 0

if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()