import cv2
import os

img = cv2.imread(os.path.join("../birds/bird.jpg"))

cv2.imwrite(os.path.join("../birds/bird-out-1.jpg"),img)

cv2.imshow("frame",img)
cv2.waitKey(0)