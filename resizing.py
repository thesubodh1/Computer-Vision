import cv2
import os


img = cv2.imread(os.path.join("../birds/bird.jpg"))
resized_image = cv2.resize(img,(500,500))
print(img.shape)
print(resized_image.shape)

cv2.imshow("Normal",img)
cv2.imshow("Resized",resized_image)
cv2.waitKey(0)