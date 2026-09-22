import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    b, g, r = cv2.split(img)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(b, cmap="gray")
    plt.axis("off")
    plt.title("Blue Channel")

    plt.subplot(1, 3, 2)
    plt.imshow(g, cmap="gray")
    plt.axis("off")
    plt.title("Green Channel")

    plt.subplot(1, 3, 3)
    plt.imshow(r, cmap="gray")
    plt.axis("off")
    plt.title("Red Channel")

    plt.show()
