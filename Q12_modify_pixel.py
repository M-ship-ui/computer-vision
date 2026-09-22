import cv2

IMAGE_PATH = "sample.jpg"
OUTPUT_PATH = "outputs/Q12_modified_pixel.jpg"

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image could not be loaded.")
else:
    height, width = img.shape[:2]
    x = int(input(f"Enter x coordinate (0 to {width-1}): "))
    y = int(input(f"Enter y coordinate (0 to {height-1}): "))
    value = int(input("Enter new intensity value (0-255): "))

    if 0 <= x < width and 0 <= y < height and 0 <= value <= 255:
        img[y, x] = value
        cv2.imwrite(OUTPUT_PATH, img)
        print("Modified pixel value:", img[y, x])
        print("Saved as:", OUTPUT_PATH)
    else:
        print("Invalid coordinate or intensity.")
