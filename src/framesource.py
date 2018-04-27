import cv2
import time

class FrameSource:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def getFrameDimension(self):
        return self.capture.get(3), self.capture.get(4)

    def grabFrame(self):
        while not self.capture.isOpened():
            time.sleep(1)
        
        check, frame = self.capture.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        return check, frame
    
    def destroy(self):
        self.capture.release()