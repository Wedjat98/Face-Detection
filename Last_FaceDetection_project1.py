import cv2 as cv
import matplotlib.pyplot as plt

# 1.读取视频
cap = cv.VideoCapture("vid/LittleGirl.mp4")
# 2.在每一帧数据中进行人脸识别
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 3.实例化OpenCV人脸识别的分类器
        face_cas = cv.CascadeClassifier("xml/haarcascade_frontalface_default.xml")
        face_cas.load('xml/haarcascade_frontalface_default.xml')
        # 4.调用识别人脸
        faceRects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        for faceRect in faceRects:
            x, y, w, h = faceRect
            # 框出人脸
            cv.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 3)
        cv.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
        cv.resizeWindow("frame", 1600, 900)  # 设置长和宽
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
# 5. 释放资源
cap.release()
cv.destroyAllWindows()
