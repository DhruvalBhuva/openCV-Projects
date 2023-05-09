'''
Thresholding is used for image segmentation. Thresholding is the simplest method of image segmentation. From a grayscale image, thresholding can be used to create binary images.
In Thresholding, we Pick a threshold T.
1.Pixels above threshold get new intensity A.
2.Pixels above threshold get new intensity B.
In Thresholding, pixels that are alike in gray scale(or in some other feature) are grouped together.
'''

import cv2 as cv
import numpy as np

img = cv.imread("gradient.png")

# threshold(<srs>,<thresh>,<maxval>,<type>,dst=none)
_, threshold1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # Till threshold value would be 0
_, threshold2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)  # inverse of above
_, threshold3 = cv.threshold(img, 127, 255,
                             cv.THRESH_TRUNC)  # till threshold value would not be changed, after rema1ins same if value is less the threshold, or if it is greter then it would be smae as threshold
_, threshold4 = cv.threshold(img, 127, 255,
                             cv.THRESH_TOZERO)  # value assigned to 0 for lower values then threshold, for greather then threshold remains same as threshold
_, threshold5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)  # Inverse of above

cv.imshow("Img", img)
# cv.imshow("Threshold 1", threshold1)
# cv.imshow("Threshold 1", threshold2)
cv.imshow("Threshold 1", threshold3)
cv.imshow("Threshold 1", threshold4)

cv.waitKey(0)
cv.destroyAllWindows()
