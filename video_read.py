import os
import cv2

video = cv2.VideoCapture(os.path.join("../videos/video.MP4"))

ret = True
while ret:
    ret,frame = video.read()

    if ret:
        cv2.imshow("Video",frame)
        cv2.waitKey(60)

video.release()
cv2.destroyAllWindows()