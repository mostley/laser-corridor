import pygame
import time

class Music:
    def __init__(self):
        self.duration = 0
        self.soundPath = './sounds/'
        self.start = 0
        pygame.init()

    def play(self, file, duration=0):
        self.duration = duration
        if pygame.mixer.music.get_busy():
            self.stop()
        pygame.mixer.music.load(self.soundPath+file)
        pygame.mixer.music.play(0)
        self.start = time.time()

    def stop(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    def checkDuration(self):
        if self.duration > 0 and time.time() - self.start > self.duration:
            self.stop()
            return True
        return False
