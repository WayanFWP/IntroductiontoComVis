import cv2
import matplotlib.pyplot as plt

# Contoh penggunaan warna RGB
img = cv2.imread('source/rubik.jpg')
# img = cv2.cvtColor(img, cv2)
print(img.shape)
# Check format warna lewat Opencv (BGR)
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
## Check format warna lewat Matplotlib (RGB)
# plt.imshow(img)
# plt.show()

## Contoh Bitwise operation
# img1 = cv2.imread('source/input1.png')  
# img2 = cv2.imread('source/input2.png')

# dest_and = cv2.bitwise_and(img2, img1, mask = None)
# dest_or = cv2.bitwise_or(img2, img1, mask = None)
# dest_xor = cv2.bitwise_xor(img2, img1, mask = None)
# dest_not = cv2.bitwise_not(img2, mask = None)

# dest_and = cv2.cvtColor(dest_and, cv2.COLOR_BGR2RGB)
# dest_or  = cv2.cvtColor(dest_or,  cv2.COLOR_BGR2RGB)
# dest_xor = cv2.cvtColor(dest_xor, cv2.COLOR_BGR2RGB)
# dest_not = cv2.cvtColor(dest_not, cv2.COLOR_BGR2RGB)

# plt.subplot(3,3,1), plt.imshow(dest_and)
# plt.title('Bitwise AND'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,6), plt.imshow(dest_or)
# plt.title('Bitwise OR'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,3), plt.imshow(dest_xor)
# plt.title('Bitwise XOR'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,4), plt.imshow(dest_not)
# plt.title('Bitwise NOT'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,2), plt.imshow(img1[:,:,::-1])
# plt.title('Input Image 1'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,5), plt.imshow(img2[:,:,::-1])
# plt.title('Input Image 2'), plt.xticks([]), plt.yticks([])
# plt.show()