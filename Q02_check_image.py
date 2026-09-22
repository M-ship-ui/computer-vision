import cv2

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Failed to load the image. Please check the file path.")
else:
    print("Success: Image loaded successfully.")
