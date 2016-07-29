import pygame as pg
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
GREY = (105, 105, 105)


FPS = 60

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 16

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

TITLE = "CLOSE THE GAP"

pg.display.set_caption("CLOSE THE GAP") 


vec = pg.math.Vector2

bgimg = pg.image.load("images/pixelpaper.jpg").convert()
bgimg = pg.transform.scale(bgimg, (800, 600))

pg.font.init()
default_font = pg.font.get_default_font()
font_renderer = pg.font.Font(default_font, 30)

# To create a surface containing `Some Text`


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.score = 0
        self.level_number = 1

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        if self.level_number == 1:
            p2 = Platform(370, 300, 150, 20)
            p3 = Platform(595, 425, 110, 20)
            p4 = Platform(145, 425, 150, 20)
            p5 = Platform(0, 500, 50, 100)
            p6 = Platform(750, 500, 50, 100)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p6)
            self.platforms.add(p6)
            self.coins = pg.sprite.Group()
            c1 = Coin(390,270)
            c2 = Coin(470, 270)
            c3 = Coin(250, 390)
            c4 = Coin(290, 320)
            c5 = Coin(170, 390)
            c6 = Coin(600, 390)
            c7 = Coin(680, 390)
            c8 = Coin(80, 425)
            c9 = Coin(560, 320)
            c10 = Coin(765, 470)
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)

        if self.level_number == 2:
            p2 = Platform(370, 300, 20, 20)
            p3 = Platform(595, 425, 20, 20)
            p4 = Platform(145, 425, 20, 20)
            p5 = Platform(0, 500, 50, 100)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.coins = pg.sprite.Group()
            c1 = Coin(390,270)
            c2 = Coin(470, 270)
            c3 = Coin(250, 390)
            c4 = Coin(290, 320)
            c5 = Coin(170, 390)
            c6 = Coin(600, 390)
            c7 = Coin(680, 390)
            c8 = Coin(80, 425)
            c9 = Coin(560, 320)
            c10 = Coin(765, 470)
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
            hits2 = pg.sprite.spritecollide(self.player, self.coins, True)
            if hits2:
                self.score += 10



        #game over
        if self.player.rect.bottom > HEIGHT:
            self.playing = False 
            pg.time.delay(100)
            self.score = 0

        if self.level_number == 1:
            if self.score == 100:
                self.level_number = 2



        


        

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        screen.blit(bgimg, [0,0])
        self.all_sprites.draw(self.screen)

        text = font_renderer.render(
            "SCORE: "+ str(self.score), True, BLACK)
        

        bgimg.blit(
            text,  # The text to render
            (10,10))  # Where on the destination surface to render said font
        # *after* drawing everything, flip the display

        pg.display.flip()



    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass



class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((70, 70))
        sprite = pg.image.load("images/girl.png").convert_alpha()
        sprite = pg.transform.scale(sprite, (70, 70))
        self.image.set_colorkey((0,0,0))
        self.image.blit(sprite, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(30, 420)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP





    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((24, 24))
        pg.draw.circle(self.image, YELLOW, (12,12), 12, 0)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


g = Game()
# g.show_start_screen()

    


while g.running:  
    g.new()
    screen.blit(bgimg, [0,0])
    pg.display.flip()
    # g.show_go_screen()




pg.quit()