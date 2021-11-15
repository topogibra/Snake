import pygame


class Snake:
  def __init__(self, display: pygame.Surface) -> None:
      self._display = display
      self._head_coords = (640,360)
      self._body = [(640,344)]
      self._speed = 16
      # Image Loading
      self._head_image = pygame.image.load("images/snakeHead.bmp")
      self._body_image = pygame.image.load("images/snakeBody.bmp")
      self._tail_image = pygame.image.load("images/snakeTail.bmp")

  def draw(self):
    # Head
    self._display.blit(self._head_image,self._head_coords)
    # Body
    for body_part_coords in self._body[:-1]:
      self._display.blit(self._body_image, body_part_coords)
    # Tail
    self._display.blit(self._tail_image, self._body[-1])

    
