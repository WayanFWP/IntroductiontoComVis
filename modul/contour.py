import cv2

img = cv2.imread('source/rubik.jpg')
real_img = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range = (0, 50, 50)
upper_range = (150, 255, 255)
mask = cv2.inRange(hsv_img, lower_range, upper_range)
color_image = cv2.bitwise_and(img, img, mask=mask)
color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)

contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:
  c = max(contours, key=cv2.contourArea)  
  rect = cv2.minAreaRect(c) 
  ((x,y), (width, height), rotation) = rect
  
  x1 = x-width/2
  y1 = y-height/2

  x2 = x+width/2
  y2 = y+height/2

  cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
  
cv2.imshow('Original Image', real_img)
cv2.imshow('Detected Color Contour', img)
cv2.imshow('Mask', mask)
cv2.imshow('Color Detected Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()