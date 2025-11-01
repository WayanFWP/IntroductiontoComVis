import cv2 

## Membaca gambar
# img = cv2.imread('source/full.jpeg') 
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## Membaca video via file
# cap = cv2.VideoCapture("source/cat.mp4")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     cv2.imshow("Video", frame)
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

## Membaca video via webcam
cap = cv2.VideoCapture(0)  # 0 = kamera default

if not cap.isOpened():
    print("Error: Tidak dapat membuka kamera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame dari kamera.")
        break

    cv2.imshow("Webcam Live", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Dihentikan oleh pengguna.")
        break

cap.release()
cv2.destroyAllWindows()