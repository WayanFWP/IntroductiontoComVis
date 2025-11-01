import cv2

img = cv2.imread("source/red.jpg")
original_height, original_width, channels = img.shape
scale = 0.5
new_height = int(original_height * scale)
new_width = int(original_width * scale)
img = cv2.resize(img, (new_width, new_height))

## Contoh membuat sebuah bentuk di gambar
maniped = img.copy()
start_point = (50, 50)
end_point = (200, 200)
color = (0, 255, 0) # Green color in BGR
thickness = 3
## Draw rectangle on the image
# maniped = cv2.rectangle(maniped, start_point, end_point, color, thickness)
## Filled blue circle
# maniped = cv2.circle(maniped, (300, 300), 50, (255, 0, 0), -1) 
## Filled hollow circle
# maniped = cv2.circle(maniped, (500, 300), 50, (0, 0, 255), 5)
## Draw Line 
maniped = cv2.line(img,(0,0),(511,511), (255,0,0), 5) 

# cv2.imshow("Original Image", img)
cv2.imshow("Manipulated Image", maniped)
cv2.waitKey(0)
cv2.destroyAllWindows()