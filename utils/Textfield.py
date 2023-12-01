import pygame
from pygame import Vector2, rect

from Game.GameObject import GameObject
from utils.utils import utils


class TextField:
    def __init__(self, rect,text = ""):
        self.rect = rect
        self.text = str(text)
        self.focus = False

    def onKeyDown(self, key):
        if not self.focus:
            return
        try:
            if key == pygame.K_BACKSPACE and len(self.text) > 0:
                self.text = self.text[:-1]
            elif int(chr(key)) in range(0,10):
                self.text += chr(key)
        except:
            return

    def draw(self):
        pygame.draw.rect(utils.screen,(99,99,99),(self.rect.x,self.rect.y,self.rect.w,self.rect.h),1)
        utils.drawText(Vector2(self.rect.x + 4,self.rect.y + 2),str(self.text),(233,233,233),font=utils.font12)

        text_width, text_height = utils.font12.size(self.text)

        if self.focus:
            pygame.draw.rect(utils.screen, (233, 233, 233), (self.rect.x + text_width + 3, self.rect.y, 1, self.rect.h), 1)