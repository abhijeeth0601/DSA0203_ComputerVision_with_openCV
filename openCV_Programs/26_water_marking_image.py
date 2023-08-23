import cv2
import numpy as np

image = cv2.imread("C:/Users/ABHIJEETH MALI/Downloads/71373969.jpg")
watermark = cv2.imread("C:/Users/ABHIJEETH MALI/Downloads/download1.jfif")

# Convert the images to grayscale.
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
watermark_gray = cv2.cvtColor(watermark, cv2.COLOR_BGR2GRAY)

# Resize the watermark image to the same size as the original image.
watermark_gray = cv2.resize(
    watermark_gray, (image_gray.shape[1], image_gray.shape[0]))

# Add the watermark image to the original image.
watermarked = cv2.addWeighted(
    image_gray, 1 - 0.4, watermark_gray, 0.2, 0, cv2.COLOR_BGR2RGB)

# Convert the watermarked image back to color.
watermarked = cv2.cvtColor(watermarked, cv2.COLOR_GRAY2BGR)

# Display the original and watermarked images.
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()
