import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded. Check IMAGE_PATH.")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.axis("off")
    plt.title("Q1 - Original Image")
    plt.show()
