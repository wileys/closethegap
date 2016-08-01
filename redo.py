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

FONT_NAME = 'arial'
vec = pg.math.Vector2

bgimg = pg.image.load("images/pixelpaper.jpg").convert()
bgimg = pg.transform.scale(bgimg, (800, 600))

pg.font.init()
default_font = pg.font.get_default_font()
font_renderer = pg.font.Font(default_font, 30)

space_KEY= pg.K_SPACE

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
        self.font_name = pg.font.match_font(FONT_NAME)
        self.score = 0
        self.level_number = 1

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        if self.level_number == 1:
            p5 = Platform(0, 500, 50, 100)
            p2 = Platform(50, 550, 800, 50)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.coins = pg.sprite.Group()
            c1 = Coin(120,520)
            c2 = Coin(190, 520)
            c3 = Coin(260, 520)
            c4 = Coin(330, 520)
            c5 = Coin(400, 520)
            c6 = Coin(470, 520)
            c7 = Coin(540, 520)
            c8 = Coin(610, 520)
            c9 = Coin(680, 520)
            c10 = Coin(750, 520)
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

        if self.level_number == 3:
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


        if self.level_number == 4:
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

        


        #white_male_platform = Platform(70, 800, 730, 20)
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



        #levels
        if self.player.rect.bottom > HEIGHT:
            self.playing = False 
            pg.time.delay(100)
            self.score = 0

        if self.level_number == 1 and self.score == 100:
                g.level_1_stats()
                # pg.time.delay(5000)
                self.level_number = 2
                self.score = 0
        
        elif self.level_number == 2 and self.score == 100:
                g.level_2_stats()
                self.level_number = 3
                self.score = 0

        elif self.level_number == 3 and self.score == 100:
                g.level_3_stats()
                self.level_number = 4
                self.score = 0

        


        

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


        screen.blit(
            text,  # The text to render
            (10,10))  # Where on the destination surface to render said font
        # *after* drawing everything, flip the display

        pg.display.flip()


    def show_start_screen(self):
        # game splash/start screen
        pass
    #def show_instructions_screen(self):
        #pass


    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                    waiting = False

    # def wait_for_K_SPACE(self):
    #     waiting = True
    #     while waiting:
    #         self.clock.tick(30)

    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 waiting = False
    #                 self.running = False
    #             if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
    #                 waiting = False

    def start_screen(self):
        self.screen.fill(WHITE)
        self.draw_text(TITLE, 75, BLACK, WIDTH/2, 200)
        self.draw_text("Press the space key to start.", 40 , BLACK, WIDTH/2, 350)
        pg.display.flip()
        self.wait_for_key()

    def instructions_screen(self):
        self.screen.fill(WHITE)
        self.draw_text("INSTRUCTIONS", 30, BLACK, WIDTH/2, 150)
        self.draw_text("USE LEFT AND RIGHT ARROW KEYS TO MOVE FORWARD AND BACK. ", 24, BLACK, WIDTH/2, 250)
        self.draw_text("USE UP ARROW KEY TO JUMP", 24, BLACK, WIDTH/2, 300)
        self.draw_text("COLLECT ALL OF THE COINS TO MOVE TO THE NEXT LEVEL AND CLOSE THE GAP!", 24, BLACK, WIDTH/2, 350)
        self.draw_text("Press the space key to start.", 24, BLACK, WIDTH/2, 450)
        pg.display.flip()
        self.wait_for_key()

    def level_1_stats(self):
        self.screen.fill(WHITE)
        self.draw_text("CONGRATULATIONS!", 30, BLACK, WIDTH/2, 150)
        self.draw_text("You have completed Level 1!. ", 24, BLACK, WIDTH/2, 250)
        self.draw_text("This level simulates climbing the ladder of success as a white male", 24, BLACK, WIDTH/2, 300)
        self.draw_text("Did you notice the lack of obstacles the man faced?", 24, BLACK, WIDTH/2, 350)
        self.draw_text("Press the space key to go to the next level.", 24, BLACK, WIDTH/2, 450)
        pg.display.flip()
        self.wait_for_key()
        

    def level_2_stats(self):
        self.screen.fill(WHITE)
        self.draw_text("CONGRATULATIONS!", 30, BLACK, WIDTH/2, 150)
        self.draw_text("You have completed Level 2!", 24, BLACK, WIDTH/2, 250)
        self.draw_text("This level simulates climbing the ladder of success as an Asian American woman", 24, BLACK, WIDTH/2, 300)
        self.draw_text("Did you notice how the money was harder to get and there were gaps between the platforms?", 24, BLACK, WIDTH/2, 350)
        self.draw_text("Asian American women generally make 90 cents to the white man's dollar.", 24,BLACK,WIDTH/2,400)
        self.draw_text("Press the space key to go to the next level.", 24, BLACK, WIDTH/2, 450)
        pg.display.flip()
        self.wait_for_key()

    def level_3_stats(self):
        self.screen.fill(WHITE)
        self.draw_text("CONGRATULATIONS!", 30, BLACK, WIDTH/2, 150)
        self.draw_text("You have completed Level 3!. ", 24, BLACK, WIDTH/2, 250)
        self.draw_text("This level simulates climbing the ladder of success as a white woman", 24, BLACK, WIDTH/2, 300)
        self.draw_text("Did you notice the money was harder to get?", 24, BLACK, WIDTH/2, 350)
        self.draw_text("White women generally make 78 cents to the white man's dollar.",24,BLACK,WIDTH/2,400)
        self.draw_text("Press the space key to go to the next level.", 24, BLACK, WIDTH/2, 450)
        pg.display.flip()
        self.wait_for_key()

    def level_4_stats(self):
        self.screen.fill(WHITE)
        self.draw_text("CONGRATULATIONS!", 30, BLACK, WIDTH/2, 150)
        self.draw_text("You have completed Level 4!. ", 24, BLACK, WIDTH/2, 250)
        self.draw_text("This level simulates climbing the ladder of success as an African American woman", 24, BLACK, WIDTH/2, 300)
        self.draw_text("Did you notice how the gaps became bigger?", 24, BLACK, WIDTH/2, 350)
        self.draw_text("African American women generally make 64 cents to the white man's dollar.",24,BLACK,WIDTH/2,400)
        self.draw_text("Press the space key to go to the next level.", 24, BLACK, WIDTH/2, 450)
        pg.display.flip()
        self.wait_for_key()


    # def go_screen():


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
g.start_screen()
g.instructions_screen()


while g.running:  
    g.new()

    screen.blit(bgimg, [0,0])
    pg.display.flip()
    # g.show_go_screen()





pg.quit()