import os
import cv2

img = cv2.imread(os.path.join("../birds/bird.jpg"))
print(img.shape)


# line
cv2.line(img,(300,700),(100,200),(0,255,0),thickness=3)

# rect
cv2.rectangle(img,(200,350),(450,600),(0,0,255),5)

# circle
cv2.circle(img,(800,100),150,(255,0,0),3)

# text
cv2.putText(img,"Hello Birds",(0,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0),3)

cv2.imshow("frame",img)
cv2.waitKey(0)