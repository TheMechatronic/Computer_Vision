import cv2
import numpy as np

def template_matching(image, template):
    # Get width and height of template
    w, h = template.shape[::-1]

    # Perform template matching
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    
    # Set a threshold for the match. Adjust this as needed.
    threshold = 0.25

    # Get the locations where matches exceed the threshold
    loc = np.where(res >= threshold)

    # Convert grayscale image to color
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Draw rectangles around matches on the main image
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image_color, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    # Show the image
    cv2.imshow('Detected', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Set the paths to the template and image
    image_path = 'Template_Matching\Images\Waldo_Map_2.jpg'
    template_path = 'Template_Matching\Images\Waldo_1.jpg'

    # Load the main image and template image - read as bgr
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    # Split the image into B,G,R channels
    B, G, R = cv2.split(image)

    # Create an array of zeros with the same shape as the image
    zeros = np.zeros_like(B)

    # Merge channels, but replace B and R channels with zeros
    green_only = cv2.merge([zeros, G, R])

    # Show the image
    cv2.imshow('Green Channel', green_only)

    # Convert the images to Greyscale
    image = cv2.cvtColor(green_only, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    template_matching(image, template)



if __name__ == "__main__":
    main()
