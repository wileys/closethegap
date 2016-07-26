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
GOLD = (255, 215, 0)
GREY = (105, 105, 105)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


start_position = (600 - SCREEN_HEIGHT, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("CLOSE THE GAP")


bgimg = pygame.image.load("images/pixelpaper.jpg").convert()
bgimg = pygame.transform.scale(bgimg, (800, 600))

pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 30)

# To create a surface containing `Some Text`
text = font_renderer.render(
    "SCORE: ",   # The font to render
    1,             # With anti aliasing
    (0,0,0)) # RGB Color

class Platform():
	def __init__ (self, color, width, height, x_position, y_position):
		self.color = color
		self.width = width
		self.height= height
		self.x_position = x_position
		self.y_position = y_position

	def drawPlatform(self):
		pygame.draw.rect(screen, self.color, (self.x_position, self.y_position, self.width, self.height), 0)


class Player():
    def __init__ (self, width, height, x_position, y_position):
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position

    def jump(self):
        y_position += 2
        x_position += 1

    def moveRight(self):
        x_position += 2

    def moveLeft(self):
        x_position -= 2


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

    def drawCoin(self):
        pygame.draw.circle(screen, self.color, (self.x_position, self.y_position), 12, 0)

    def drawCash(self):
        cash = pygame.image.load("images/money.gif")
        cash = pygame.transform.scale(cash, (50, 50))
        cash.convert_alpha()
        bgimg.blit(cash, (735,375))





done = False

while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.blit(bgimg, [0, 0])


    coin1 = Coin(GOLD, 175, 400)
    coin1.drawCoin()
    coin2 = Coin(GOLD, 240, 400)
    coin2.drawCoin()
    coin3 = Coin(GOLD, 305, 400)
    coin3.drawCoin()
    coin4 = Coin(GOLD, 325, 315)
    coin4.drawCoin()
    coin5 = Coin(GOLD, 425, 315)
    coin5.drawCoin()
    coin6 = Coin(GOLD, 525, 315)
    coin6.drawCoin()
    coin7 = Coin(GOLD, 615, 290)
    coin7.drawCoin()
    coin8 = Coin(GOLD, 635, 400)
    coin8.drawCoin()
    coin9 = Coin(GOLD, 700, 400)
    coin9.drawCoin()
    coin1.drawCash()
    # start_platform =  platform.drawPlatform()
    platform1 = Platform(GREY, 200, 30, 370, 350)
    platform1.drawPlatform()
    platform2 = Platform(GREY, 200, 30, 595, 425)
    platform2.drawPlatform()
    platform3 = Platform(GREY, 200, 30, 145, 425)
    platform3.drawPlatform()
    platform4 = Platform(GREY, 100, 200, 0, 500)
    platform4.drawPlatform()
    # platform2 = platform.drawPlatform()
    # platorm3 = platform.drawPlatform()
    # endplatform = platform.drawPlatform()


    player = Player(120, 120, 0, SCREEN_HEIGHT - 120)
    player.drawSprite()

    bgimg.blit(
    text,  # The text to render
    (10,10))  # Where on the destination surface to render said font


    pygame.display.flip()


pygame.quit()
exit()

# OUR LOVELY CODE WILL GO HERE.