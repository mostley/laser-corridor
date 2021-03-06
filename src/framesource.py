import cv2
import time

class FrameSource:
    def __init__(self):
        self.inputVideo = 0
        self.minTreshBinary = 200
        self.capture = cv2.VideoCapture(self.inputVideo)

    def getFrameDimension(self):
        return self.capture.get(3), self.capture.get(4)

    def grabFrame(self):
        while not self.capture.isOpened():
            time.sleep(1)
        
        check, frame = self.capture.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.threshold(frame, self.minTreshBinary, 255, cv2.THRESH_BINARY)[1]
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        return check, frame
    
    def destroy(self):
        self.capture.release()