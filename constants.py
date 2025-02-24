import pygame

pygame.init()
FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
MOVE_VEL = 20

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
