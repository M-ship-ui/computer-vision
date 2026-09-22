import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.axis("off")
    plt.title("Q9 - Matplotlib Display")
    plt.show()
