import pygame

pygame.init()
#Define colors 
BLACK = (0, 0, 0)
WHITE =(255, 255, 255) 
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
GREY = (105, 105, 105)



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


start_position = (600 - SCREEN_HEIGHT, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("CLOSE THE GAP")

pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 30)
intro_font = pygame.font.Font(default_font, 100)

intro = intro_font.render(
    "Close the Gap",
    1,
    (0,0,0))

while True:
    screen.fill((255, 255, 255))

