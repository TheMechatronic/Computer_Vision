import cv2
import numpy as np

def template_matching(image, template):
    # Get width and height of template
    w, h = template.shape[::-1]

    # Perform template matching
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    
    # Set a threshold for the match. Adjust this as needed.
    threshold = 0.4

    # Get the locations where matches exceed the threshold
    # loc = np.where(res >= threshold)

    # Get the location where the maximum match is
    # Find the location of the maximum response
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    print(max_val)

    # Convert grayscale image to color
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cropped_image = image[max_loc[1]:max_loc[1]+h, max_loc[0]:max_loc[0]+w]
    # Add red rectangle around identified area
    cv2.rectangle(  image_color,    # target image
                    max_loc,        # top right corner
                    (max_loc[0]+w, max_loc[1]+h),   #left bottom corner
                    (0,0,255),      # frame colour
                    2)              # line thickness

    # Show the image
    cv2.imshow('Detected', image_color)
    cv2.imshow('Detected Frame', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Set the paths to the template and image
    image_path = 'Template_Matching\Images\Waldo_Map_1.jpg'
    template_path = 'Template_Matching\Images\Waldo_1.jpg'

    # Load the main image and template image - read as bgr
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    # Split the image into B,G,R channels
    B, G, R = cv2.split(image)

    # Create an array of zeros with the same shape as the image
    zeros = np.zeros_like(B)

    # Merge channels, but replace B and R channels with zeros
    green_only = cv2.merge([zeros, zeros, R])

    # Split the image into B,G,R channels
    B, G, R = cv2.split(template)

    # Create an array of zeros with the same shape as the image
    zeros = np.zeros_like(B)

    # Merge channels, but replace B and R channels with zeros
    green_only_template = cv2.merge([zeros, zeros, R])

    # Show the image
    # cv2.imshow('Green Channel', green_only)
    # Show the image
    # cv2.imshow('Green Channel 2', green_only_template)

    # Convert the images to Greyscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    template_matching(image, template)



if __name__ == "__main__":
    main()
