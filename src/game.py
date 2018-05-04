from detector import Detector
from framesource import FrameSource
from music import Music
from window import Window

import cv2

class Game:
    def __init__(self):
        self.running = False
        self.detector = Detector()
        self.frameSource = FrameSource()
        self.music = Music()
        self.window = Window()

        self.duration = 10
        self.currentKeypoints = None
        self.previousKeypoints = None

    def run(self):
        self.running = True
        self.music.play('mi-full.wav', 10)

        while self.running:
            if self.music.checkDuration():
                self.music.play('siren.wav')

            check, frame = self.frameSource.grabFrame()

            if not check:
                print("no frame found!")
                continue

            self.previousKeypoints = self.currentKeypoints
            self.currentKeypoints, frame_with_keypoints = self.detector.detect(frame)

            self.window.showFrame(frame_with_keypoints)

            if self.previousKeypoints != None:
                self.update()
            
            key = cv2.waitKey(50)
            if key == ord('q'):
                break


    def update(self):
        pass
    
    def destroy(self):
        self.frameSource.destroy()
        self.window.destroy()

if __name__ == '__main__':
    print("Starting Game")
    game = Game()
    game.run()
    game.destroy()
    print("Game ended")