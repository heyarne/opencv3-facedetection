import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier()
if not face_cascade.load('./share/haarcascades/haarcascade_frontalface_default.xml'):
    print('Face cascade could not be initialized, pleace check the path')
    cap.release()
    exit(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    try:
        faces = face_cascade.detectMultiScale(gray, 1.3)
        for (x, y, w, h) in faces: # draw all found faces
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    except:
        pass

    # Display the resulting frame, quit on q
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
