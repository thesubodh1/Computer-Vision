import cv2
import os
import numpy as np



img = cv2.imread(os.path.join("../birds/bird.jpg"))
# grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_edge = cv2.Canny(img,100,200)
img_edge_dilate = cv2.dilate(img_edge,np.ones(shape=(2,2),dtype=np.int8))
img_edge_erode = cv2.erode(img_edge_dilate,np.ones(shape=(3,3),dtype=np.int8))


cv2.imshow("Frame",img)
cv2.imshow("canny",img_edge)
cv2.imshow("canny_dilate",img_edge_dilate)
cv2.imshow("canny_dilate_erode",img_edge_erode)


cv2.waitKey(0)