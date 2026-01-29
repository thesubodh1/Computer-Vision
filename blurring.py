import cv2
import os

img = cv2.imread(os.path.join("../birds/bird.jpg"))
k_size = 7 # Higher the number more blur
blurred_1 = cv2.blur(img,(k_size,k_size),5)
gaussian_blur = cv2.GaussianBlur(img,(k_size,k_size),5)
median_blur = cv2.medianBlur(img,k_size)

cv2.imshow("Blurred_1",blurred_1)
cv2.imshow("Gaussian Blur",gaussian_blur)
cv2.imshow("Median Blur",median_blur)
cv2.waitKey(0)