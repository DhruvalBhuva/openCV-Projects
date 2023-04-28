import cv2

'''=>  Read video and open it '''

'''
video = cv2.VideoCapture("D:\Image\Dhruval\video.mp4")
print("video", video)

while True:
    ret, frame = video.read()  # read() returen ret  as True if frame is avilable
    print("Frame", frame

    print("Width: ", cv2.CAP_PROP_FRAME_WIDTH)
    print("Height: ", cv2.CAP_PROP_FRAME_HEIGHT)
    # for More properties: https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

    frame = cv2.resize(frame, (700, 450))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameFlip = cv2.flip(frame, -1)

    cv2.imshow("ColorFrame", frame)
    cv2.imshow("Gray Frame", gray)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows() 
'''

# '''
#=> Open video camera, record that video and save it '''
 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
print("checking..",cap.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
outputPath = "output.avi"
fps=20.0
height,weight=640,480

#It contain 4 parameter , name, codec,fps,resolution
outputObj = cv2.VideoWriter(outputPath,fourcc,fps,(height,weight),0)

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,0)
        outputObj.write(gray)
        
        cv2.imshow("Gray Frame", gray)
        cv2.imshow("Color Frame:", frame)
        
        if cv2.waitKey(25) == ord("q"):
            break
    else:
        break
    
# Release everything if job is finished
cap.release()
outputObj.release()
cv2.destroyAllWindows()
# '''