import cv2

img=cv2.imread("ronaldo.jpg", 0)

cv2.imshow("First image", img)

k=cv2.waitKey(0) & 0xFF

if k==27:#27 esc'ye denk
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("ronaldogri.png", img)
    