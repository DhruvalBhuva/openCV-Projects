import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg",-1)
cv.imshow("Cv2 Image", img)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB) # Matplot uses RGB formate so need to transalate it
plt.imshow(img)  

plt.xticks([]),plt.yticks([]) # To hide X,Y axis

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()