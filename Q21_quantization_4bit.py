import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("Error: Image could not be loaded.")
else:
    quantized_4bit = (gray // 16) * 16
    quantized_4bit = quantized_4bit.astype(np.uint8)

    print("Number of unique displayed levels:", len(np.unique(quantized_4bit)))

    plt.imshow(quantized_4bit, cmap="gray", vmin=0, vmax=255)
    plt.axis("off")
    plt.title("Q21 - 4-bit Quantized Image")
    plt.show()
