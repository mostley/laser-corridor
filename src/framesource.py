from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time

class FrameSource:
    def __init__(self):
        self.minTreshBinary = 200
        self.camera = picamera.PiCamera()
        self.capture = self.camera.capture()

    def grabFrame(self):
        self.camera.start_preview()
        time.sleep(2)
        
        frame = self.camera.capture("bgr")

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.threshold(frame, self.minTreshBinary, 255, cv2.THRESH_BINARY)[1]
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        return check, frame
    
    def destroy(self):
        self.camera.close()