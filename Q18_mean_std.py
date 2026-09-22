import cv2
import numpy as np

IMAGE_PATH = "sample.jpg"
gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("Error: Image could not be loaded.")
else:
    mean_intensity = np.mean(gray)
    std_intensity = np.std(gray)

    print("Mean intensity:", mean_intensity)
    print("Standard deviation:", std_intensity)
