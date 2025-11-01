import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('source/rubik.jpg')
real_img = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range = (0, 50, 50)
upper_range = (150, 255, 255)
mask = cv2.inRange(hsv_img, lower_range, upper_range)
color_image = cv2.bitwise_and(img, img, mask=mask)
color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)

contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:
  c = max(contours, key=cv2.contourArea)  
  rect = cv2.minAreaRect(c) 
  ((x,y), (width, height), rotation) = rect
  
  x1 = x-width/2
  y1 = y-height/2

  x2 = x+width/2
  y2 = y+height/2
  
  colored_contours = np.zeros_like(img)
  for i, cnt in enumerate(contours):
    color = (0, 255 - (i * 15) % 256, (i * 30) % 256)
    cv2.drawContours(colored_contours, contours, i, color, thickness=3, lineType=cv2.LINE_AA)
  
plt.subplot(1,3,1)
plt.imshow(real_img[:,:,::-1])
plt.title('Original Image'), plt.xticks([]), plt.yticks([]) 
plt.subplot(1,3,2)
plt.imshow(mask, cmap='gray')
plt.title('Mask Image'), plt.xticks([]), plt.yticks([]) 
plt.subplot(1,3,3)
plt.imshow(colored_contours[:,:,::-1])
plt.title('Color Detected Image'), plt.xticks([]), plt.yticks([])
plt.show()