##Game takes about 2 min 30 seconds to load (a really long time so please be patient)
##Still need to add hot block functions, laser functions, ball collection, score,
##moving animal

import pygame
from pygame.locals import *
import sys
import pygame.mixer
import random
import constants
import levels

from ball import Ball
from player import Player
from player2 import Player2

class Score1:
    def __init__(self):
        self.score1 = 0
        self.font = pygame.font.SysFont("Britannic Bold", 50)

    def draw(self, screen):
        player1_score = self.font.render("Player1 Score: " + str(self.score1), True, (constants.WHITE))
        screen.blit(player1_score, (0, 0))

    def add(self):
        self.score1 += 1

class Score2:
    def __init__(self):
        self.score2 = 0
        self.font = pygame.font.SysFont("Britannic Bold", 50)
    
    def draw(self, screen):
        player2_score = self.font.render("Player2 Score: " + str(self.score2), True, (constants.WHITE))
        screen.blit(player2_score, (1090, 0))

    def add(self):
        self.score2 += 1

def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size, FULLSCREEN, 32)

    sound = pygame.mixer.music.load("BBT background.ogg")
#    sound = pygame.mixer.music.load("BUCKLE ur PANTS.ogg")
    pygame.mixer.music.play(-1,0.0)

    pygame.display.set_caption("Pyblock Theater")
 
    # Create the player
    player = Player()
    player2 = Player2()
    ball = Ball()
    score1 = Score1()
    score2 = Score2()
     
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_01(player2))
    level_list.append(levels.Level_01(ball))
    
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    player2.level = current_level
    ball.level = current_level

    player_rect = pygame.Rect(player.rect.x, player.rect.y, 72, 70)
    player2_rect = pygame.Rect(player2.rect.x, player2.rect.y, 72, 70)
    
    player.rect.x = 75
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - 25
    player2.rect.x = 1266
    player2.rect.y = constants.SCREEN_HEIGHT - player2.rect.height - 25
    ball.rect.x = random.randint(1, 1291)
    ball.rect.y = random.randint(1, 718)

    active_sprite_list.add(player, player2, ball)
    
    #Current player scores
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    pygame.mouse.set_visible(0)

    # -------- Main Program Loop -----------
    #Loop until the user clicks the close button.
    Start_game = True
    done = False
    while (1):
        if Start_game == True and done == False:
            bg = pygame.transform.scale(pygame.image.load("background_1.jpg"),(1366, 768))
            myfont = pygame.font.SysFont("Britannic Bold", 50)
            title = myfont.render("Welcome to PYBLOCK THEATER", True, (constants.WHITE))
            control1 = myfont.render("Player 1 Controls: Arrow Keys", True, (constants.WHITE))
            control2 = myfont.render("Player 2 Controls: WASD", True, (constants.WHITE))
            start = myfont.render("Press Left Mouse to Start", True, (constants.WHITE))
            
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    done = True
                    Start_game = False
                    break
                
            screen.blit(bg, (0, 0))
            screen.blit(title, (420,180))
            screen.blit(control1, (450, 300))
            screen.blit(control2, (450, 400))
            screen.blit(start, (483, 600))
            
            pygame.display.flip()
        
        elif Start_game == False and done == True:
            
            while (done == True):
                   
                for event in pygame.event.get(): # User did something
                    
                    if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        done = True
                        pygame.quit()
                        sys.exit() # If user clicked close
                         # Flag that we are done so we exit this loop
         
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.go_left()
                        if event.key == pygame.K_RIGHT:
                            player.go_right()
                        if event.key == pygame.K_UP:
                            player.jump()
         
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and player.change_x < 0:
                            player.stop()

                        if event.key == pygame.K_RIGHT and player.change_x > 0:
                            player.stop()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            player2.go_left()
                        if event.key == pygame.K_d:
                            player2.go_right()
                        if event.key == pygame.K_w:
                            player2.jump()
         
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a and player2.change_x < 0:
                            player2.stop()

                        if event.key == pygame.K_d and player2.change_x > 0:
                            player2.stop()

                    if player.rect.colliderect(ball.rect):
                        active_sprite_list.remove(ball)
                        active_sprite_list.update()
                        score1.add()
                        score1.draw(screen)
                        current_level.draw(screen)
                        active_sprite_list.draw(screen)
                        pygame.display.update()
                        ball.rect.x = random.randint(1, 1291)
                        ball.rect.y = random.randint(1, 743)
                        active_sprite_list.add(ball)
                        active_sprite_list.update()
                        current_level.draw(screen)
                        active_sprite_list.draw(screen)
                        pygame.display.update()

                    elif player2.rect.colliderect(ball.rect):
                        active_sprite_list.remove(ball)
                        active_sprite_list.update()
                        score2.add()
                        score2.draw(screen)
                        current_level.draw(screen)
                        active_sprite_list.draw(screen)
                        pygame.display.update()
                        ball.rect.x = random.randint(1, 1291)
                        ball.rect.y = random.randint(1, 743)
                        active_sprite_list.add(ball)
                        active_sprite_list.update()
                        current_level.draw(screen)
                        active_sprite_list.draw(screen)
                        pygame.display.update()
                        


                # Update the player.
                active_sprite_list.update()
         
                # Update items in the level
                current_level.update()
         
                # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
                current_level.draw(screen)
                active_sprite_list.draw(screen)
                score1.draw(screen)
                score2.draw(screen)


                # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
                
                # Limit to 60 frames per second
                clock.tick(60)
         
                # Go ahead and update the screen with what we've drawn.
                pygame.display.flip()
         
            # Be IDLE friendly. If you forget this line, the program will 'hang'
            # on exit.
            pygame.quit()
         
if __name__ == "__main__":
    main()
