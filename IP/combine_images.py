import cv2
import numpy as np

img = cv2.imread("ronaldo.jpg")

hor= np.hstack((img,img))
cv2.imshow("Horizontal copy",hor)

ver = np.vstack((img,img))
cv2.imshow("Vertical copy",ver)