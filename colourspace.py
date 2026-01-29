import os

import cv2

img = cv2.imread(os.path.join("./birds/bird.jpg"))
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.imshow("frame",img)
cv2.imshow("fra me_rbg",img_rgb)
cv2.imshow("frame_grey",img_grey)
cv2.imshow("frame_hsv",img_hsv)
cv2.waitKey(0)