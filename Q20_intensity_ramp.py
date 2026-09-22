import numpy as np
import matplotlib.pyplot as plt

ramp_row = np.arange(256, dtype=np.uint8)
intensity_ramp = np.tile(ramp_row, (256, 1))

plt.imshow(intensity_ramp, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.title("Q20 - Grayscale Intensity Ramp")
plt.show()

print("Minimum:", intensity_ramp.min())
print("Maximum:", intensity_ramp.max())
