import cv2

face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./xml/haarcascade_smile.xml')

img = cv2.imread('./image/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,   # 檢測粒度
    minNeighbors=10,   # 每個目標至少偵測到幾次以上才被認定
    minSize=(30, 30),  # 搜尋的最小尺寸
    flags=cv2.CASCADE_SCALE_IMAGE  # 針對影像
)

print("faces: ", len(faces), faces)

for (x, y, w, h) in faces:
    # 繪文字 putText(來源, 文字, 左下座標, 字型, 字型大小, 文字顏色, 文字線條寬度)
    cv2.putText(img, 'Anita', (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    # 畫框
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    #-------------------------------------------------------------

    roi_gray = gray[y:y + h, x:w + h]
    roi_img  =  img[y:y + h, x:w + h]

    smile = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,   # 檢測粒度
        minNeighbors=10,   # 每個目標至少偵測到幾次以上才被認定
        minSize=(30, 30),  # 搜尋的最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE  # 針對影像
    )
    cv2.rectangle(roi_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # -------------------------------------------------------------

cv2.imshow('Face', img)
cv2.waitKey(0)
