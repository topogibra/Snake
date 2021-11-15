import operator
from collections import deque
from typing import Tuple
import pygame


class Snake:
    def __init__(self, display: pygame.Surface) -> None:
        self._display = display
        # Head coordinates
        self._default_speed = 16
        self._speed = self._default_speed
        self._head_coords = (display.get_width() // 2,
                             display.get_height() // 2 - 8)
        self._body_coords = deque()
        self._body_coords.append(
            (self._head_coords[0], self._head_coords[1] - self._speed))
        self._movement = (0, self._speed)
        self.eat = False
        # Image Loading
        self._head_image = pygame.image.load("images/snakeHead.bmp")
        self._body_image = pygame.image.load("images/snakeBody.bmp")
        self._tail_image = pygame.image.load("images/snakeTail.bmp")

        self.head = self._head_image.get_rect()

    def sumTuples(self, a: Tuple, b: Tuple):
        # return tuple(map(operator.add, a, b)
        [width, height] = self._display.get_size()
        return (
            (a[0] + b[0]) % width,
            (a[1] + b[1]) % height
        )

    def draw(self):
        # Head
        self.head = self._display.blit(self._head_image, self._head_coords)
        # Body
        self.body = []
        for body_part_coords in self._body_coords:
            self.body.append(self._display.blit(
                self._body_image, body_part_coords))

    def can_move(self, movement: Tuple):
        return self.sumTuples(self._head_coords, movement) != self._body_coords[0]

    def move_update(self):
        new_head_coords = self.sumTuples(self._head_coords, self._movement)
        if self.can_move(self._movement):
            self._body_coords.appendleft(self._head_coords)
            self._head_coords = new_head_coords
            if not self.eat:
                self._body_coords.pop()
            else:
                self.eat = False

    def left(self):
        movement = (-self._speed, 0)
        self._movement = movement if self.can_move(
            movement) else self._movement

    def right(self):
        movement = (self._speed, 0)
        self._movement = movement if self.can_move(
            movement) else self._movement

    def up(self):
        movement = (0, -self._speed)
        self._movement = movement if self.can_move(
            movement) else self._movement

    def down(self):
        movement = (0, self._speed)
        self._movement = movement if self.can_move(
            movement) else self._movement

    def grow(self):
        self.eat = True

    def can_spawn_fruit(self,position: Tuple):
      return position != self._head_coords and position not in self._body_coords

    def hit_body(self):
      return self._head_coords in self._body_coords