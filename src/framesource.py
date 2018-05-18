from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import io
import numpy as np

class FrameSource:
    def __init__(self):
	self.minTreshBinary = 200
	self.stream = io.BytesIO()
        self.camera = PiCamera()
        self.rawCapture = PiRGBArray(self.camera)
	self.camera.start_preview()
	self.camera.resolution = (1280, 960)
	time.sleep(1)

    def grabFrame(self):
	self.camera.capture(self.rawCapture, format='bgr')
	frame = self.rawCapture.array
	self.rawCapture.truncate(0)

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      	frame = cv2.threshold(frame, self.minTreshBinary, 255, cv2.THRESH_BINARY)[1]
	frame = cv2.GaussianBlur(frame, (5, 5), 0)
	return frame

    def destroy(self):
        self.camera.close()
