import cv2
import numpy as np

class Detector:
    def __init__(self):
        is_v2 = cv2.__version__.startswith("2.")
        params = cv2.SimpleBlobDetector_Params()

        if is_v2:
            self.detector = cv2.SimpleBlobDetector(params)
        else:
            self.detector = cv2.SimpleBlobDetector_create(params)

    def detect(self, frame):
        # keypoints = self.detector.detect(frame)
        retval, threshold = cv2.threshold(frame, 50, 255, cv2.THRESH_BINARY_INV)
        keypoints = self.detector.detect(threshold)

        frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        return keypoints, frame_with_keypoints
