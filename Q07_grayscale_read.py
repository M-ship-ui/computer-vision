import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("Error: Image could not be loaded.")
else:
    plt.imshow(gray, cmap="gray")
    plt.axis("off")
    plt.title("Q7 - Grayscale Image")
    plt.show()
