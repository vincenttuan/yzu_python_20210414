import cv2

face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')

img = cv2.imread('./image/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("faces: ", len(faces), faces)

