import cv2
import numpy as np

img = cv2.imread("card.png")
cv2.imshow("Org",img)
width=400
height=500
edges1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
edges2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(edges1,edges2)
imgP=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Perspective changed",imgP)
