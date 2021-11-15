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
        self._movement = (self._default_speed, 0)
        # Image Loading
        self._head_image = pygame.image.load("images/snakeHead.bmp")
        self._body_image = pygame.image.load("images/snakeBody.bmp")
        self._tail_image = pygame.image.load("images/snakeTail.bmp")

    def sumTuples(a: Tuple, b: Tuple):
        return tuple(map(operator.add, a, b))

    def draw(self):
        # Head
        self._display.blit(self._head_image, self._head_coords)
        # Body
        for body_part_coords in self._body:
            self._display.blit(self._body_image, body_part_coords)
        # Tail
        # self._display.blit(self._tail_image, self._body[-1])

    def can_move(self, movement: Tuple):
        return Snake.sumTuples(self._head_coords, movement) != self._body[0]

    def move_update(self):
        new_head_coords = Snake.sumTuples(self._head_coords, self._movement)
        if self.can_move(self._movement):
            self._body.appendleft(self._head_coords)
            self._head_coords = new_head_coords
            self._body.pop()

    def left(self):
        movement = (-self._default_speed, 0)
        self._movement = movement if self.can_move(
            movement) else self._movement

    def right(self):
        movement = (self._default_speed, 0)
        self._movement = movement if self.can_move(
            movement) else self._movement

    def up(self):
        movement = (0, -self._default_speed)
        self._movement = movement if self.can_move(
            movement) else self._movement

    def down(self):
        movement = (0, self._default_speed)
        self._movement = movement if self.can_move(
            movement) else self._movement
