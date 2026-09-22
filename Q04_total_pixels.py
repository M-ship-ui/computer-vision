import cv2

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    height, width = img.shape[:2]
    total_pixels = height * width
    print("Total number of pixels:", total_pixels)
