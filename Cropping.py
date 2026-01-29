import cv2
import os

img = cv2.imread(os.path.join("../birds/bird.jpg"))
cropped_img = img[100:400,500:900] #(height, width)

cv2.imshow("Cropped",cropped_img)
cv2.waitKey(0)