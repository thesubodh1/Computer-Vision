import cv2
import os



img = cv2.imread(os.path.join("../birds/re-sky.jpg"))

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,10)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 100:
        x1,y1,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),3)



cv2.imshow("sky",img)

cv2.waitKey(0)