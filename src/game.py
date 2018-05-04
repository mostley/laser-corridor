from detector import Detector
from finishsounds import Finishsounds
from framesource import FrameSource
from music import Music
from window import Window

import cv2


class Game:
    def __init__(self):
        self.running = False
        self.isPaused = False
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
        self.start()

        while self.running:
            key = cv2.waitKey(50)
            if key == ord('q'):
                break
            elif key == ord(' ') and not self.isPaused:
                self.finish(Finishsounds.success)
            elif key == ord('s'):
                self.start()
            elif key == ord('p'):
                self.togglepause()
            elif key == ord('e'):
                self.stop()

            if self.isPaused:
                continue

            if self.music.playtime_finished():
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

            if self.previousKeypoints is not None:
                self.update()

    def start(self):
        self.running = True
        self.isPaused = False
        self.numKeypoints = len(self.getkeypoints())
        self.music.play(self.soundtrackFile, self.duration)
        print('New game started')

    def togglepause(self):
        self.music.togglepause()
        if self.isPaused:
            print('Game resumed')
        else:
            print('Game paused')
        self.isPaused = not self.isPaused

    def stop(self):
        self.isPaused = True
        self.music.stop()
        print('Game stopped')

    def finish(self, result):
        if not self.music.currentFile == self.soundtrackFile:
            return
        soundfile = self.finishSounds[result]
        print('Game ended on ' + result.name + ' after ' + str(self.music.get_playtime()) + ' seconds ')
        self.music.play(soundfile)

    def update(self):
        pass

    def getkeypoints(self):
        check, frame = self.frameSource.grabFrame()
        keypoints, frame_with_keypoints = self.detector.detect(frame)
        return keypoints
    
    def destroy(self):
        self.music.destroy()
        self.frameSource.destroy()
        self.window.destroy()

if __name__ == '__main__':
    print('Starting Game')
    game = Game()
    game.run()
    game.destroy()
    print('Game ended')