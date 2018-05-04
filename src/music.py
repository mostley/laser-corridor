import pygame
import time


class Music:
    def __init__(self):
        self.isPaused = False
        self.duration = 0
        self.soundPath = './sounds/'
        self.currentFile = ''
        self.start = 0
        pygame.init()

    def play(self, file, duration=0):
        self.duration = duration

        if pygame.mixer.music.get_busy():
            self.stop()

        self.currentFile = file
        pygame.mixer.music.load(self.soundPath+file)
        pygame.mixer.music.play(0)
        self.start = time.time()

    def togglepause(self):
        if pygame.mixer.music.get_busy():
            if self.isPaused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            self.isPaused = not self.isPaused

    def stop(self):
        if pygame.mixer.music.get_busy():
            self.currentFile = ''
            pygame.mixer.music.stop()

    def playtime_finished(self):
        is_finished = self.duration > 0 and time.time() - self.start > self.duration
        return is_finished

    def get_playtime(self):
        playtime = 0
        if pygame.mixer.music.get_busy():
            playtime = time.time() - self.start
        playtime = round(playtime, 2)
        return playtime


    def destroy(self):
        pygame.mixer.quit()
