from random import randint
from pygame import Surface
import pygame


class Fruit:
    def __init__(self, display: Surface):
        self._display = display
        self._image = pygame.image.load("images/fruit.bmp")
        self.rect = self._image.get_rect()
        self.coords = self.randomPosition()
        pass

    def randomPosition(self):
        x = randint(0, (self._display.get_width() - 1) // 16) * 16
        y = randint(0, (self._display.get_height() - 1) // 16) * 16
        return (x,y)
        

    def draw(self):
        self.rect = self._display.blit(self._image, self.coords)
