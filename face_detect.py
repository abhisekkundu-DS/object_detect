import cv2
import mediapipe as mp
import time

# cap = cv2.VideoCapture(r"C:\Users\Abhisek kundu\Downloads\\Face_detect.mp4 ")
cap = cv2.VideoCapture(0)
pTime = 0
#Face Detection
mpFaceDetection = mp.solutions.face_detection
mpDraw =  mp.solutions.drawing_utils
FaceDetection = mpFaceDetection.FaceDetection()



while True:
    success, img = cap.read()
    # cv2.imshow("Image",img)

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = FaceDetection.process(imgRGB)
    print(results)



    if results.detections:
        for id ,detection in enumerate(results.detections):
            # mpDraw.draw_detection(img,detection)
            # print(id,detection)
            # print(detection.score)
            # auto draw a box detect from this picture 
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih ,iw , ic = img.shape
            bbox  = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img , bbox,(255,0,255),2)




    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'Fps:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(200,255,0),2)
    cv2.imshow("Image", img)


    cv2.waitKey(20)
