import cv2

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    height, width, channels = img.shape
    print("Height:", height)
    print("Width:", width)
    print("Number of channels:", channels)
