import cv2

class Window:
    def __init__(self):
        pass

    def showFrame(self, frame):
        cv2.imshow("Game", frame)
    
    def destroy(self):
        cv2.destroyAllWindows()