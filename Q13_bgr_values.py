import cv2

IMAGE_PATH = "sample.jpg"
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    height, width = img.shape[:2]
    x = int(input(f"Enter x coordinate (0 to {width-1}): "))
    y = int(input(f"Enter y coordinate (0 to {height-1}): "))

    if 0 <= x < width and 0 <= y < height:
        b, g, r = img[y, x]
        print("B:", int(b))
        print("G:", int(g))
        print("R:", int(r))
    else:
        print("Error: Coordinate is outside the image.")
