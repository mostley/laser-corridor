from detector import Detector
from finishsounds import Finishsounds
from framesource import FrameSource
from music import Music
from window import Window
from input import Input
import cv2


class Game:
    def __init__(self):
        self.running = False
        self.isPaused = False
        self.detector = Detector()
        self.frameSource = FrameSource()
        self.music = Music()
        self.window = Window()
	self.input = Input()

        self.finishSounds = {
            Finishsounds.success: 'mario-victory.wav',
            Finishsounds.failure: 'siren.wav',
            Finishsounds.timeIsUp: 'buzzer.wav'
        }
        self.soundtrackFile = 'mi-full.wav'
        self.duration = 30
        self.numKeypoints = 0
        self.currentKeypoints = None
        self.previousKeypoints = None

    def run(self):
        self.start()

        while self.running:
	    switch = self.input.isSwitchToggled()
            self.keyHandler(switch)
	    button = self.input.readButton()
            #key = cv2.waitKey(50)
            self.keyHandler(button)
	    self.keyHandler(self.input.readQuitButton())
            if self.isPaused:
                continue

            if self.music.playtimeFinished():
                self.finish(Finishsounds.timeIsUp)

            frame = self.frameSource.grabFrame()

            self.previousKeypoints = self.currentKeypoints
            self.currentKeypoints, frame_with_keypoints = self.detector.detect(frame)
	    #print(len(self.currentKeypoints))
	    self.window.showFrame(frame_with_keypoints)

            if len(self.currentKeypoints) != self.numKeypoints:
                self.finish(Finishsounds.failure)

            if self.previousKeypoints is not None:
                self.update()

    def start(self):
        self.running = True
        self.isPaused = False
        self.numKeypoints = len(self.getKeypoints())
        self.music.play(self.soundtrackFile, self.duration)
        print('New game started')

    def togglePause(self):
        self.music.togglePause()
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
        if self.music.currentFile == self.soundtrackFile:
            soundfile = self.finishSounds[result]
            print('Game ended on ' + result.name + ' after ' + str(self.music.getPlaytime()) + ' seconds ')
            self.music.play(soundfile)

    def update(self):
        pass

    def getKeypoints(self):
        frame = self.frameSource.grabFrame()
        keypoints, frame_with_keypoints = self.detector.detect(frame)
        return keypoints

    def keyHandler(self, key):
	#print(key)
        # Start game
        if key == 'Start':
            self.start()
        # Pause/resume game
        #elif key == ord('p'):
        #    self.togglePause()
        # End game
        elif key == 'Stopp':
            self.stop()
        # Quit game
        elif key == 'Quit':
            self.running = False
        # Trigger succeed event
        elif key == 'Pressed' and not self.isPaused:
            self.finish(Finishsounds.success)


    def destroy(self):
        self.music.destroy()
        self.frameSource.destroy()
        #self.window.destroy()

if __name__ == '__main__':
    print('Starting Game')
    game = Game()
    game.run()
    game.destroy()
    print('Game ended')
