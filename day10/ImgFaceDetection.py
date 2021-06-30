import cv2

face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')

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
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Face', img)
cv2.waitKey(0)
