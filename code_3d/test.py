import cv2
# reading the image using imread
image = cv2.imread("img.jpg", 0)

# extracting with and height of image

# h, w = image.shape[:2]
# print(f"Height={h}, width = {w}")
cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()