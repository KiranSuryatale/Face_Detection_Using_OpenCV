import cv2

face_detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

def detect_faces(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )

    return faces