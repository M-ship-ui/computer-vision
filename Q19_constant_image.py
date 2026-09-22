import cv2
import numpy as np
import matplotlib.pyplot as plt

constant_image = np.full((256, 256), 128, dtype=np.uint8)

plt.imshow(constant_image, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.title("Q19 - Intensity 128")
plt.show()

print("Shape:", constant_image.shape)
print("Unique intensity values:", np.unique(constant_image))
