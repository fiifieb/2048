import pygame
import random
import math
from constants import *
from draw import *
from logic import *


pygame.init()


def run(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                handle_press(event.key, window, clock)

        draw(window, tiles)

    pygame.quit()


if __name__ == "__main__":
    run(WINDOW)
