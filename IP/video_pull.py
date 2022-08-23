import cv2
import time

video_name = "video.mp4"

cap = cv2.VideoCapture(video_name)

print("Gen: ",cap.get(3))
print("Height: ",cap.get(4))

if cap.isOpened() == False:#Always use this if statement to check everthing is ok
    print("Hata")

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.001)#kullanmazsak çok hızlı akar
        cv2.imshow("Video",frame)
    else: break

    if cv2.waitKey(2) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()