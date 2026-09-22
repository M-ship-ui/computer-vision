import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    original_height, original_width = img.shape[:2]
    new_width = original_width // 2
    new_height = original_height // 2

    downsampled = cv2.resize(img, (new_width, new_height))

    print("Original resolution:", original_width, "x", original_height)
    print("New resolution:", new_width, "x", new_height)

    plt.imshow(cv2.cvtColor(downsampled, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Q23 - Downsampled Image")
    plt.show()
