import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("Error: Image could not be loaded.")
else:
    quantized_2bit = (gray // 64) * 64
    quantized_2bit = quantized_2bit.astype(np.uint8)

    print("Number of unique displayed levels:", len(np.unique(quantized_2bit)))

    plt.imshow(quantized_2bit, cmap="gray", vmin=0, vmax=255)
    plt.axis("off")
    plt.title("Q22 - 2-bit Quantized Image")
    plt.show()
