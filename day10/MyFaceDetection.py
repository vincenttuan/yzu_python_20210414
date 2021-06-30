import cv2

face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')

# 設定 Webcam 位置
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # 1024
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 768

while True:
    # ret: True/False
    # img : 每一個 frame 區域資料
    ret, img = cap.read()
    print(ret, img)

    img = cv2.flip(img, 1)  # 鏡像處理

    # 人臉偵測並畫紅框 ------------------------

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # 檢測粒度
        minNeighbors=10,  # 每個目標至少偵測到幾次以上才被認定
        minSize=(30, 30),  # 搜尋的最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE  # 針對影像
    )

    print("faces: ", len(faces), faces)

    for (x, y, w, h) in faces:
        # 繪文字 putText(來源, 文字, 左下座標, 字型, 字型大小, 文字顏色, 文字線條寬度)
        cv2.putText(img, 'Vincent', (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        # 畫框
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # 顯示在 ui 上
    cv2.imshow('My face', img)

    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

# 釋放資源
cap.release()
cv2.destroyAllWindows()
