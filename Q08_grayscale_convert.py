import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray, cmap="gray")
    plt.axis("off")
    plt.title("Q8 - Grayscale using cvtColor")
    plt.show()
