'''
Thresholding is used for image segmentation. Thresholding is the simplest method of image segmentation. From a grayscale image, thresholding can be used to create binary images.
In Thresholding, we Pick a threshold T.
1.Pixels above threshold get new intensity A.
2.Pixels above threshold get new intensity B.
In Thresholding, pixels that are alike in gray scale(or in some other feature) are grouped together.
'''
# Otsu's Binarization: Automatically calculates threshold value from image histogram for a bimodal image.
# cv.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
# cv.THRESH_BINARY_INV: Inverted or Opposite case of cv.THRESH_BINARY.
# cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. The pixel values are set to be the same as the threshold. All other values remain the same.
# cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
# cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv.THRESH_TOZERO.
# cv.THRESH_MASK: It is not a thresholding technique, but a mask that is used to extract part of an array.
# cv.THRESH_OTSU: Otsu's thresholding method, to automatically calculate threshold value from image histogram for a bimodal image.
# cv.THRESH_TRIANGLE: Triangle thresholding method, to automatically calculate threshold value from image histogram for a bimodal image.

import cv2 as cv
import numpy as np

'''
# img = cv.imread("gradient.png")

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
# cv.imshow("Threshold 2", threshold2)
# cv.imshow("Threshold 3", threshold3)
# cv.imshow("Threshold 4", threshold4)
# cv.imshow("Threshold 5", threshold5)

'''


''' ==>> Adeptive Thresold: Diffrent thresold value for different region of img.'''
img = cv.imread('sudoku.png',0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)


# adaptiveThreshold(<ImgObj>,<Max value>,<adeptive method>,<thresold type>, <blocksize>, C, Dst=None)

# Adaptive Methods: 
# cv.ADAPTIVE_THRESH_MEAN_C: The thresold value T(x,y) is a mean of the blocksize * BlockSize neighborthood of (x,y) c.
# cv.ADAPTIVE_THRESH_GAUSSIAN_C: The thresold value T(x,y) is a weighted sum of the blocksize * BlockSize neighborthood of (x,y) c.

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);

cv.imshow("Image", img)
cv.imshow("THRESH_BINARY", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)


cv.waitKey(0)
cv.destroyAllWindows()
