import cv2
import time
import numpy

class FrameSource:
    def __init__(self):
        self.capture = cv2.VideoCapture(1)

    def getFrameDimension(self):
        return self.capture.get(3), self.capture.get(4)

    def grabFrame(self):
        while not self.capture.isOpened():
            time.sleep(1)
        
        check, frame = self.capture.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.threshold(frame, 160, 255, cv2.THRESH_BINARY)[1]
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        return check, frame
    
    def destroy(self):
        self.capture.release()