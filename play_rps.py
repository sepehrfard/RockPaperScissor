from fastai.vision import *
from fastai.metrics import error_rate
import os
import cv2

cap = cv2.VideoCapture(0)
learner = load_learner('','rps.pkl')
labels = ['paper', 'rock', 'scissor']
idx_check = 10
idx = 0
while cap.isOpened():
    ret, frame = cap.read()
    idx += 1

    if ret == True:
        frame = cv2.flip(frame, 180)
        frame = frame[120:600, 400:880]
        if idx % idx_check == 0:
            idx = 0
            t = torch.tensor(
                np.ascontiguousarray(np.flip(frame, 2)).transpose(2, 0, 1)).float() / 255
            img = Image(t)
            p = learner.predict(img)
            print(p[0])

        cv2.imshow("frame", frame)
        if (cv2.waitKey(1) & 0xFF) == ord("q"):  # Hit `q` to exit
            break
    else:
        break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()


