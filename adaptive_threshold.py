import cv2
import os

img = cv2.imread(os.path.join("../birds/bird.jpg"))
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(grey_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)


cv2.imshow("Grey",grey_img)
cv2.imshow("Adaptive",adaptive_threshold)
cv2.waitKey(0)