import cv2

img = cv2.imread("ronaldo.jpg",0)
print(img.shape)
cv2.imshow("orj",img)

#resize
resized_ronaldo = cv2.resize(img,(800,800))
cv2.imshow("res",resized_ronaldo)

#cut
cropped_ronaldo = img[:200,:300]
cv2.imshow("Cutted Ronaldo",cropped_ronaldo)