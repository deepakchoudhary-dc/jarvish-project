import cv2
import numpy as np

def cartoonize_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Resize the image
    image = cv2.resize(image, (960, 540))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to reduce noise while preserving edges
    filtered = cv2.bilateralFilter(image, 9, 250, 250)

    # Apply adaptive thresholding to create a binary image
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Perform color quantization to reduce the number of colors
    num_colors = 16
    indices = np.arange(0, 256)
    div = np.linspace(0, 255, num_colors+1)[1]
    quantized = np.int0(np.divide(gray, div)) * div
    quantized = cv2.cvtColor(quantized, cv2.COLOR_GRAY2BGR)

    # Apply bilateral filter to the quantized image for smoother color transitions
    quantized = cv2.bilateralFilter(quantized, 9, 250, 250)

    # Apply median blur to smooth out the image
    ksize = 7
    blurred = cv2.medianBlur(quantized, ksize)

    # Create a mask by combining the edges and color quantization
    mask = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(blurred, mask)

    # Enhance the cartoonized image using bilateral filter and sharpening
    enhanced = cv2.bilateralFilter(cartoon, 9, 250, 250)
    enhanced = cv2.addWeighted(cartoon, 1.5, enhanced, -0.5, 0)
    enhanced = cv2.GaussianBlur(enhanced, (9, 9), 0)

    # Apply stylization to the enhanced image for a more artistic look
    stylized = cv2.stylization(enhanced, sigma_s=60, sigma_r=0.6)

    # Display the original, cartoonized, and stylized images
    cv2.imshow("Original Image", image)
    cv2.imshow("Cartoonized Image", cartoon)
    cv2.imshow("Stylized Image", stylized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Provide the path to your image
image_path = "C:\\Users\\mrrr7\\Downloads\\VIT_blockchain_img-transformed.png"

# Call the function to cartoonize the image
cartoonize_image(image_path)


