import pygame

class Music:
    def __init__(self):
        self.soundPath = './sounds/'
        pygame.init()

    def play(self, file, duration, callback=None):
        pygame.mixer.music.load(self.soundPath+file)
        pygame.mixer.music.play(0)
        if callback:
            callback()

    def stop(self):
        pygame.mixer.music.stop()