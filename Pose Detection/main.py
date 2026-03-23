import cv2
import mediapipe as mp

BaseOption = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
Image = mp.Image
ImageFormat = mp.ImageFormat

MODEL_PATH = "pose_landmarker_full.task"

options  = PoseLandmarkerOptions(base_options=BaseOption(model_asset_path=MODEL_PATH),running_mode=VisionRunningMode.VIDEO)

landmarker = PoseLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    mp_image = Image(ImageFormat.SRGB,data=rgb_frame)

    time_stamp = int(cv2.getTickCount() / cv2.getTickFrequency() * 1000)

    result = landmarker.detect_for_video(mp_image,time_stamp)

    if result.pose_landmarks:
        for pose in result.pose_landmarks:
            for lm in pose:
                x = int(lm.x * frame.shape[1])
                y = int(lm.y * frame.shape[0])
                cv2.circle(frame,(x,y),1,(0,255,0),3)
                
    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()