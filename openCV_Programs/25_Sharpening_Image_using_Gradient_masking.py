import cv2
import numpy as np


def main():
    # Load the image.
    image = cv2.imread("C:/Users/ABHIJEETH MALI/Downloads/71373969.jpg")

    # Apply Gaussian blur.
    kernel_size = 5
    blurred = np.zeros_like(image)
    for i in range(image.shape[0] - kernel_size + 1):
        for j in range(image.shape[1] - kernel_size + 1):
            blurred[i: i + kernel_size, j: j + kernel_size] = cv2.filter2D(
                image[i: i + kernel_size, j: j + kernel_size], -1,
                cv2.getGaussianKernel(kernel_size, 0))

    # Display the original and blurred images.
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
