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
        #self.camera = PiCamera()
        #self.rawCapture = PiRGBArray(self.camera)
	#self.camera.resolution = (640, 480)
	time.sleep(1)

    def grabFrame(self):
	with PiCamera() as camera:
		camera.start_preview()
		camera.resolution = (320, 240)
		camera.framerate = 24
		time.sleep(2)
		image = np.empty((240 * 320 * 3,), dtype=np.uint8)
		camera.capture(image, 'bgr')
		#camera.capture(self.stream, 'jpeg')
		#buff = np.fromstring(self.stream.getvalue(), dtype=np.uint8)
		#frame = cv2.imdecode(buff, 1)

		frame = image.reshape((240, 320, 3))
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      	 	frame = cv2.threshold(frame, self.minTreshBinary, 255, cv2.THRESH_BINARY)[1]
		return frame

    def destroy(self):
        self.camera.close()
