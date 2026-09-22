import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "sample.jpg"
OUTPUT_PATH = "outputs/Q24_cropped_roi.jpg"

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    height, width = img.shape[:2]

    x1 = int(input(f"Enter x1 (0 to {width-1}): "))
    y1 = int(input(f"Enter y1 (0 to {height-1}): "))
    x2 = int(input(f"Enter x2 ({x1+1} to {width}): "))
    y2 = int(input(f"Enter y2 ({y1+1} to {height}): "))

    if 0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height:
        roi = img[y1:y2, x1:x2]

        plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
        plt.axis("off")
        plt.title("Q24 - Cropped ROI")
        plt.show()

        cv2.imwrite(OUTPUT_PATH, roi)
        print("ROI saved as:", OUTPUT_PATH)
        print("ROI resolution:", roi.shape[1], "x", roi.shape[0])
    else:
        print("Invalid coordinates.")
