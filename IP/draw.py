import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)#512,512,3 is the size of the img and uint8 is the key to numbers to be integer
print(img.shape)

cv2.imshow("image",img)

#LINE
cv2.line(img,(0,0),(512,512),(0,255,0),3)#image, start point, finish point and color(BGR=Blue Green Red), thickness
cv2.imshow("Line",img)

#SQUARE
cv2.rectangle(img,(0,0),(256,256),(255,0,0))#image, start point, finish point and color
cv2.imshow("Square",img)

#CIRCLE
cv2.circle(img,(300,300),30,(0,0,255))#image, circle radius start point, radius, color
cv2.imshow("Circle",img)

cv2.putText(img,"HELLO WORLD",(250,250),cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255))#image,word,location,font,thickness,color
cv2.imshow("Word",img)