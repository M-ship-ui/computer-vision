import cv2

IMAGE_PATH = "sample.jpg"
OUTPUT_PATH = "outputs/Q06_saved_image.jpg"

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    success = cv2.imwrite(OUTPUT_PATH, img)
    print("Image saved successfully:", success)
    print("Saved as:", OUTPUT_PATH)
