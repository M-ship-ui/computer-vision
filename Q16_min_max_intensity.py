import cv2
import numpy as np

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image could not be loaded.")
else:
    print("Minimum intensity:", np.min(img))
    print("Maximum intensity:", np.max(img))
