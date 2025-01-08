import cv2
import numpy as np

def sample_image():
    # Import a sample image from the dataset (content/training/00000/00000_00000.jpg)
    img = cv2.imread("content/training/00000/00000_00000.jpg")
    return img

def sharpen_image(image):
    # Convert the image to RGB format (assuming it's in BGR)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a sharpening kernel
    kernel = np.array([[-1, 0, -1],
                       [0, 8, 0],
                       [-1, 0, -1]])

    # Apply the sharpening kernel using cv2.filter2D
    sharpened = cv2.filter2D(image_rgb, -1, kernel)

    return sharpened

def unsharp_mask(image):
    # Apply Gaussian blur to the image
    blurred = cv2.GaussianBlur(image, (0, 0), 2.0)
    # Create a mask by subtracting the blurred image from the original image
    sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
    return sharpened

def threshold_image(image):
    # Convert the image to grayscale
    _, thresholded = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    return thresholded

def contrast_stretching(image):
    # Convert the image to RGB format (assuming it's in BGR)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate minimum and maximum pixel values
    min_val = image_rgb.min(axis=(0, 1))
    max_val = image_rgb.max(axis=(0, 1))

    # Check if max_val and min_val are equal for any channel
    equal_min_max = np.all(min_val == max_val)

    # Perform contrast stretching only if min_val and max_val are not equal
    stretched = np.zeros_like(image_rgb, dtype=np.uint8)
    if not equal_min_max:
        stretched = ((image_rgb - min_val) * 255) // (max_val - min_val)

    return stretched

def morphological_operations(image):
    # Create a 3x3 kernel
    kernel = np.ones((3, 3), np.uint8)
    # Perform dilation followed by erosion
    dilated = cv2.dilate(image, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    return eroded

def main():
    img = sample_image()
    sharpened = sharpen_image(img)
    unsharp_masked = unsharp_mask(img)
    thresholded = threshold_image(img)
    contrast_stretched = contrast_stretching(img)
    morphological = morphological_operations(img)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Sharpened Image", sharpened)
    cv2.imshow("Unsharp Masked Image", unsharp_masked)
    cv2.imshow("Thresholded Image", thresholded)
    cv2.imshow("Contrast Stretched Image", contrast_stretched)
    cv2.imshow("Morphological Operations Image", morphological)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()