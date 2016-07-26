import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


start_position = (600 - SCREEN_HEIGHT, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("CLOSE THE GAP")


bgimg = pygame.image.load("images/pixelpaper.jpg").convert()
bgimg = pygame.transform.scale(bgimg, (800, 600))


class Player():
    def __init__ (self, width, height, x_position, y_position):
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position

    
    def drawSprite(self):
        sprite = pygame.image.load("images/running.png")
        sprite = pygame.transform.scale(sprite, (self.width, self.height))
        sprite.convert_alpha()
        bgimg.blit(sprite, (self.x_position, self.y_position))
       # pygame.draw.rect(screen, self.color, [0, 0, self.width, self.height])

    def jump(self):
        y_position += 2
        x_position += 1

    def moveRight(self):
        x_position += 2

    def moveLeft(self):
        x_position -= 2

    



class Coin():
    def __init__ (self, color, x_position, y_position):
        self.color = color
        self.x_position = x_position
        self.y_position = y_position

    def createCoin(self):
        pygame.draw.circle(screen, self.color, (self.x_position, self.y_position), 20, 0)




done = False

while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.blit(bgimg, [0, 0])

    player = Player(120, 120, 0, SCREEN_HEIGHT - 120)
    player.drawSprite()



    pygame.display.flip()


pygame.quit()
exit()

# OUR LOVELY CODE WILL GO HERE.