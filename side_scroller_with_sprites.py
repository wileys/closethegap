import pygame
import random
# importing the Scroller to use as background
from scroller import Scroller as Scroller



    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

class Block(pygame.sprite.Sprite):

    def __init__(self, file_name):
        super().__init__()

        # Loading the sprite from the file
        
        self.image = pygame.image.load(file_name)

        # This sets the background of the image.
        # Setting it to white makes it so that it blends in the rest of screen
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = random.randrange(0, screen_height)
            self.rect.x = screen_width + 10


pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

bad_sprites_list = pygame.sprite.Group()

good_sprites_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()
player = Block("Melissa.png")

# This makes the 

def make_sprites(level):
    '''
    This makes the sprites.
    The level argument is used to decide how many bad sprites there are
    '''

    all_sprites_list.add(player)
    
    for i in range(50):   
        good_sprite = Block("Balloon.png")
        
        

        good_sprite.rect.x = random.randrange(screen_width, screen_width * 2)
        good_sprite.rect.y = random.randrange(screen_height)

       
        good_sprites_list.add(good_sprite)

        all_sprites_list.add(good_sprite)

    for i in range(10 * level):
        bad_sprite = Block("Bee.png")
        
        bad_sprite.rect.x = random.randrange(screen_width, screen_width * 2)
        bad_sprite.rect.y = random.randrange(screen_height)

        bad_sprites_list.add(bad_sprite)
        all_sprites_list.add(bad_sprite)



# This will clear out all the sprites when the game has ended
def empty():
    all_sprites_list.empty()
    bad_sprites_list.empty()
    good_sprites_list.empty()
    


done = False

clock = pygame.time.Clock()

score = 0

lives = 5

## The scroller object is created here
any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)

## Font to allow for 
font = pygame.font.SysFont("Gill Sans", 25, True, False)

level = 1

# Blocks for first run of game
make_sprites(level)

# Variable to check if pressing r will restart game
can_restart = False

# Variable to check if pressing n will go on to the next level
next_level = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and can_restart:
                score = 0
                lives = 5
                level = 1
                make_sprites(level)
                can_restart = False
            elif event.key == pygame.K_n and next_level:
                lives = 5
                level += 1
                make_sprites(level)
                next_level = False


 
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.midright = pos
 
    # See if the player block has collided with anything.
    bad_sprites_hit_list = pygame.sprite.spritecollide(player, bad_sprites_list, True)
    good_sprites_hit_list = pygame.sprite.spritecollide(player, good_sprites_list, True)

    # Move the blocks.
    bad_sprites_list.update()
    good_sprites_list.update()
 
    # Check the list of collisions.
    for block in good_sprites_hit_list:
        score += 1

    for block in bad_sprites_hit_list:
        lives -= 1

    score_text = font.render("Score: " +str(score), True, BLACK)

    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    screen.blit(score_text, [500, 50])

    screen.blit(lives_text, [50, 50])

    ## Some logic to allow the game to be restarted

    # Check if there are any good sprites left.
    # If not then offer to go on to the next level
    if  len(good_sprites_list) == 0 and lives >= 1:
        empty()
        beat_level = font.render("Congratulations you beat level " + str(level), True, BLACK)
        next_level = font.render("Press 'n' to play the next level", True, BLACK)
        screen.blit(beat_level, [150, 100])
        screen.blit(next_level, [150, 150])
        next_level = True
    
    if lives < 1:
        empty()
        game_over = font.render("Game Over!", True, BLACK)
        play_again = font.render("Press 'r' to play again", True, BLACK)
        screen.blit(game_over, [150, 100])
        screen.blit(play_again, [150, 150])
        can_restart = True
    
    # Draw the scrolling background
    any_scroller.draw_buildings(screen)
    any_scroller.move_buildings()

    
    # Draw all the sprites  
    all_sprites_list.draw(screen)




   
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

