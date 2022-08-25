import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

writer = cv2.VideoWriter("Video_record.mp4", cv2.VideoWriter_fourcc(*"DIVX"),30,(width, height))#fourcc compresses windows on 'windows op'

if cap.isOpened == False:
    print("Error")
    
while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Camera",frame)
        writer.write(frame)
    else: break

    if cv2.waitKey(1) &  0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()