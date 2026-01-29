import cv2
import os

img = cv2.imread(os.path.join("../birds/bird.jpg"))

grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(grey_img,135,255,cv2.THRESH_BINARY)


cv2.imshow("Grey",grey_img)
cv2.imshow("Threshold",thresh)
cv2.waitKey(0)