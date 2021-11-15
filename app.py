from curses import KEY_RIGHT
import pygame
from pygame.locals import *

from snake import Snake


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1280, 720

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.snake = Snake(self._display_surf)
        self._running = True
        self._image_surf = pygame.image.load("images/snakeBody.bmp")
        self._snake_ticks = 300
        self._last_ticks = pygame.time.get_ticks()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT] or keys[K_d]:
                self.snake.right()
            if keys[K_LEFT] or keys[K_a]:
                self.snake.left()
            if keys[K_UP] or keys[K_w]:
                self.snake.up() 
            if keys[K_DOWN] or keys[K_s]:
                self.snake.down()

    def on_loop(self):
        current_ticks = pygame.time.get_ticks()
        if abs(self._last_ticks - current_ticks) >= self._snake_ticks:
            self._last_ticks = current_ticks
            self.snake.move_update()

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.snake.draw()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
