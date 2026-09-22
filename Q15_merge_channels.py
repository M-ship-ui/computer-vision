import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    b, g, r = cv2.split(img)
    merged = cv2.merge([b, g, r])

    plt.imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Q15 - Merged BGR Image")
    plt.show()

    print("Merge successful:", np.array_equal(img, merged))
