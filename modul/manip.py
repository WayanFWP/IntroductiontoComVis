import cv2

# img = cv2.imread("source/full.jpeg")
img = cv2.imread("source/red.jpg")

## Contoh nge Resize gambar
original_height, original_width, channels = img.shape
scale = 0.5
new_height = int(original_height * scale)
new_width = int(original_width * scale)
# maniped = cv2.resize(img, (new_width, new_height))
img = cv2.resize(img, (new_width, new_height))

# Contoh nge Zoom gambar
center_x, center_y = img.shape[1] // 2, img.shape[0] // 2
zoom_factor = 1.5
new_width = int(img.shape[1] / zoom_factor)
new_height = int(img.shape[0] / zoom_factor)
x1 = center_x - new_width // 2
y1 = center_y - new_height // 2
x2 = x1 + new_width
y2 = y1 + new_height
cropped_img = img[y1:y2, x1:x2]
maniped = cv2.resize(cropped_img, (img.shape[1], img.shape[0]))

## Contoh Roi Manipulation
# x, y, w, h = 100, 100, 200, 200
# roi = img[y:y+h, x:x+w] #  ROI coordinates (x: 100-300, y: 100-300)
# maniped = img.copy()
# manipulated_roi = cv2.GaussianBlur(roi, (15, 15), 0)
# # manipulated_roi = roi.copy()
# ## Example manipulation: Convert ROI to grayscale
# maniped[y:y+h, x:x+w] = manipulated_roi

## Contoh nge Rotate gambar
# center = (img.shape[1] // 2, img.shape[0] // 2)
# angle = 45
# scale = 1.0
# rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
# maniped = cv2.warpAffine(img, rotation_matrix, (img.shape[1], img.shape[0]))


cv2.imshow("Original Image", img)
cv2.imshow("Manipulated Image", maniped)
cv2.waitKey(0)
cv2.destroyAllWindows()