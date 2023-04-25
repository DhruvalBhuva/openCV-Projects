import cv2

#connect your laptop and android device with same network either wifi or hotspot
# add this IP into browser to open on lptop
cameraIP = "https://192.168.0.15:8080/video"

#Here parameter 0 is a path of any video use for webcam
cap = cv2.VideoCapture(0)
cap.open(cameraIP)

print("Cam check:", cap.isOpened())

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

#It contain 4 parameter , name, codec,fps,resolution
outputObj = cv2.VideoWriter("Cam_video.mp4", fourcc, 20.0, (680, 400))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.resize(frame, (700, 600))
        outputObj.write(frame)
        
        cv2.imshow('Colorframe',frame)
        
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

cap.release()
outputObj.release()
cv2.destroyAllWindows()