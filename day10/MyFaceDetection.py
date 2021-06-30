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




    # 顯示在 ui 上
    cv2.imshow('My face', img)

    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

# 釋放資源
cap.release()
cv2.destroyAllWindows()
