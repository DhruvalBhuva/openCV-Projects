import cv2
import numpy as np


# events= [i for i in dir(cv2) if "EVENT" in i]  # dir fun used to show all the classes and fun of library
# print(events)

def click_event_fun(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " , ", y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + " " + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow("Image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]  # It gives blue clr
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + " " + str(green) + " " + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 225), 2)
        cv2.imshow("Image", img)


img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("lena.jpg")

# window name should be same in all the imshow
cv2.imshow("Image", img)

cv2.setMouseCallback('Image', click_event_fun)

cv2.waitKey(0)
cv2.destroyAllWindows()
