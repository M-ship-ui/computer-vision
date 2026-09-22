import cv2

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    print("Image data type:", img.dtype)
