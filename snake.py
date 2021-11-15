import operator
from collections import deque
from typing import Tuple
import pygame


class Snake:
    def __init__(self, display: pygame.Surface) -> None:
        self._display = display
        self._head_coords = (640, 360)
        self._body = deque()
        self._body.append((640, 344))
        self._default_speed = 16
        # Image Loading
        self._head_image = pygame.image.load("images/snakeHead.bmp")
        self._body_image = pygame.image.load("images/snakeBody.bmp")
        self._tail_image = pygame.image.load("images/snakeTail.bmp")
    
    def sumTuples(a:Tuple,b:Tuple):
      return tuple(map(operator.add,a,b))

    def draw(self):
        # Head
        self._display.blit(self._head_image, self._head_coords)
        # Body
        for body_part_coords in self._body:
            self._display.blit(self._body_image, body_part_coords)
        # Tail
        # self._display.blit(self._tail_image, self._body[-1])

    def move_update(self, movement: Tuple):
        new_head_coords = Snake.sumTuples(self._head_coords,movement)
        if new_head_coords != self._body[0]:
          self._body.appendleft(self._head_coords)
          self._head_coords = new_head_coords
          self._body.pop()

    def left(self):
        self.move_update((-self._default_speed, 0))
        
    def right(self):
        self.move_update((self._default_speed, 0))

    def up(self):
        self.move_update((0, -self._default_speed))
    
    def down(self):
        self.move_update((0, self._default_speed))
