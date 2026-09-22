import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    height, width = img.shape[:2]
    new_width = int(width * 0.5)
    new_height = int(height * 0.5)

    resized = cv2.resize(img, (new_width, new_height))

    print("Original resolution:", width, "x", height)
    print("New resolution:", new_width, "x", new_height)

    plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Q10 - 50% Resized Image")
    plt.show()
