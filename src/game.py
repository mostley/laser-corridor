from detector import Detector
from finishsounds import Finishsounds
from framesource import FrameSource
from music import Music
from window import Window

import cv2
import time

class Game:
    def __init__(self):
        self.running = False
        self.detector = Detector()
        self.frameSource = FrameSource()
        self.music = Music()
        self.window = Window()

        self.finishSounds = {
            Finishsounds.success: 'mario-victory.wav',
            Finishsounds.failure: 'siren.wav',
            Finishsounds.timeIsUp: 'buzzer.wav'
        }
        self.soundtrackFile = 'mi-full.wav'
        self.duration = 10
        self.currentKeypoints = None
        self.previousKeypoints = None
        self.numKeypoints = 0

    def run(self):
        self.numKeypoints = len(self.getStartKeypoints())
        self.running = True
        self.music.play(self.soundtrackFile, self.duration)

        while self.running:
            if self.music.checkDuration():
                self.finish(Finishsounds.timeIsUp)

            check, frame = self.frameSource.grabFrame()

            if not check:
                print("no frame found!")
                continue

            self.previousKeypoints = self.currentKeypoints
            self.currentKeypoints, frame_with_keypoints = self.detector.detect(frame)

            self.window.showFrame(frame_with_keypoints)

            if len(self.currentKeypoints) != self.numKeypoints:
                self.finish(Finishsounds.failure)

            if self.previousKeypoints != None:
                self.update()
            
            key = cv2.waitKey(50)
            if key == ord('q'):
                break

            key = cv2.waitKey(32)
            if key == ord(' '):
                self.finish(Finishsounds.success)

    def finish(self, result):
        soundfile = self.finishSounds[result]
        self.music.play(soundfile)
        time.sleep(3)
        self.running = False


    def getStartKeypoints(self):
        check, frame = self.frameSource.grabFrame()
        keypoints, frame_with_keypoints = self.detector.detect(frame)
        return keypoints

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