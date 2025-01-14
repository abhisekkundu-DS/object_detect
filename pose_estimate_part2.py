import cv2
import mediapipe as mp
import time

from scipy.special import lmbda

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(r'C:\Users\Abhisek kundu\Downloads\\videoplayback.mp4')
pTime = 0
while True:
    success, img = cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    print(result.pose_landmarks)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h,w,c = img.shape
            print(id,lm)


    # cv2.imshow("Image",img)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Image",img)
    cv2.waitKey(40)
