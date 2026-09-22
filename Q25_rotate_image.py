import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
OUTPUT_PATH = "outputs/Q25_rotated_90.jpg"

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(OUTPUT_PATH, rotated)

    plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Q25 - Rotated 90 Degrees")
    plt.show()

    print("Rotated image saved as:", OUTPUT_PATH)
