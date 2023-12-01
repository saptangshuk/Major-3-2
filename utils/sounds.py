import pygame

class Sounds:
    def __init__(self):
        pygame.mixer.init()

        self.ss = {
            'click': pygame.mixer.Sound("assets/clickBtn.wav")
        }
        pygame.mixer.music.load("assets/music.wav")
        pygame.mixer.music.play(-1)


    def play(self, key):
        pygame.mixer.Sound.play(self.ss[key])


mSounds = Sounds()
