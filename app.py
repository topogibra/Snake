from curses import KEY_RIGHT
import pygame
from pygame.locals import *
from fruit import Fruit

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
        self._running = True

        self.fruit_coutner = 0

        self.snake = Snake(self._display_surf)
        self._snake_ticks = 200
        self._shift_speed_up = False
        self._last_ticks = pygame.time.get_ticks()

        self.fruit = Fruit(self._display_surf)

    def on_event(self):
        if pygame.event.get(pygame.QUIT):
            self._running = False
        if  pygame.event.get(pygame.KEYDOWN):
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT] or keys[K_d]:
                self.snake.right()
            if keys[K_LEFT] or keys[K_a]:
                self.snake.left()
            if keys[K_UP] or keys[K_w]:
                self.snake.up()
            if keys[K_DOWN] or keys[K_s]:
                self.snake.down()
            if keys[K_q]:
                self.fruit.coords = self.fruit.randomPosition()
            if keys[K_LSHIFT] and not self._shift_speed_up:
                self._snake_ticks = self._snake_ticks // 20
                self._shift_speed_up = True
        event = pygame.event.get(pygame.KEYUP)
        if event:
            if event[0].key == K_LSHIFT:
                self._snake_ticks = self._snake_ticks * 20
                self._shift_speed_up = False

    def on_loop(self):
        # move snake along with time
        current_ticks = pygame.time.get_ticks()
        if abs(self._last_ticks - current_ticks) >= self._snake_ticks:
            self._last_ticks = current_ticks
            self.snake.move_update()

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.snake.draw()
        self.fruit.draw()
        # colide detection
        if self.snake.hit_body():
            self._running = False
        if self.fruit.rect.colliderect(self.snake.head):
            print("Snake ate fruit @ ", self.snake._head_coords)
            self.snake.grow()
            randomPosition = self.fruit.randomPosition()
            while not self.snake.can_spawn_fruit(randomPosition):
                randomPosition = self.fruit.randomPosition()
            self.fruit.coords = randomPosition
            # increase game speed
            new_speed = self._snake_ticks - 10
            self._snake_ticks = new_speed if new_speed >= 100 else self._snake_ticks
        
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
