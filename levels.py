import pygame
 
import constants
import platforms
 
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
 
        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None
 
        # Background image
        self.background = None
 
        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.world_shift // 3,0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
    
    def shift_world_y(self, shift_y):
        
        self.world_shift += shift_y
        
        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.transform.scale(pygame.image.load("background_4.png").convert_alpha(), (1366,768))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
 
        # Array with type of platform, and x, y location of the platform.
        level = [#Bottom Border

                  [platforms.RED_MIDDLE, -9, 743],
                  [platforms.RED_MIDDLE, 16, 743],
                  [platforms.RED_MIDDLE, 41, 743],
                  [platforms.RED_MIDDLE, 66, 743],
                  [platforms.RED_MIDDLE, 91, 743],
                  [platforms.RED_MIDDLE, 116, 743],
                  [platforms.RED_MIDDLE, 141, 743],
                  [platforms.RED_MIDDLE, 166, 743],
                  [platforms.RED_MIDDLE, 191, 743],
                  [platforms.RED_MIDDLE, 216, 743],
                  [platforms.RED_MIDDLE, 241, 743],
                  [platforms.RED_MIDDLE, 266, 743],
                  [platforms.RED_MIDDLE, 291, 743],
                  [platforms.RED_MIDDLE, 316, 743],
                  [platforms.RED_MIDDLE, 341, 743],
                  [platforms.RED_MIDDLE, 366, 743],
                  [platforms.RED_MIDDLE, 391, 743],
                  [platforms.RED_MIDDLE, 416, 743],
                  [platforms.RED_MIDDLE, 441, 743],
                  [platforms.RED_MIDDLE, 466, 743],
                  [platforms.RED_MIDDLE, 491, 743],
                  [platforms.RED_MIDDLE, 516, 743],
                  [platforms.RED_MIDDLE, 541, 743],
                  [platforms.RED_MIDDLE, 566, 743],
                  [platforms.RED_MIDDLE, 591, 743],
                  [platforms.RED_MIDDLE, 616, 743],
                  [platforms.RED_MIDDLE, 641, 743],
                  [platforms.RED_MIDDLE, 666, 743],
                  [platforms.RED_MIDDLE, 691, 743],
                  [platforms.RED_MIDDLE, 716, 743],
                  [platforms.RED_MIDDLE, 741, 743],
                  [platforms.RED_MIDDLE, 766, 743],
                  [platforms.RED_MIDDLE, 791, 743],
                  [platforms.RED_MIDDLE, 816, 743],
                  [platforms.RED_MIDDLE, 841, 743],
                  [platforms.RED_MIDDLE, 866, 743],
                  [platforms.RED_MIDDLE, 891, 743],
                  [platforms.RED_MIDDLE, 916, 743],
                  [platforms.RED_MIDDLE, 941, 743],
                  [platforms.RED_MIDDLE, 966, 743],
                  [platforms.RED_MIDDLE, 991, 743],
                  [platforms.RED_MIDDLE, 1016, 743],
                  [platforms.RED_MIDDLE, 1041, 743],
                  [platforms.RED_MIDDLE, 1066, 743],
                  [platforms.RED_MIDDLE, 1091, 743],
                  [platforms.RED_MIDDLE, 1116, 743],
                  [platforms.RED_MIDDLE, 1141, 743],
                  [platforms.RED_MIDDLE, 1166, 743],
                  [platforms.RED_MIDDLE, 1191, 743],
                  [platforms.RED_MIDDLE, 1216, 743],
                  [platforms.RED_MIDDLE, 1241, 743],
                  [platforms.RED_MIDDLE, 1266, 743],
                  [platforms.RED_MIDDLE, 1291, 743],
                  [platforms.RED_MIDDLE, 1316, 743],
                  [platforms.RED_MIDDLE, 1341, 743],

                  #Right Border
                  [platforms.RED_MIDDLE, 1341, 743],
                  [platforms.RED_MIDDLE, 1341, 718],
                  [platforms.RED_MIDDLE, 1341, 693],
                  [platforms.RED_MIDDLE, 1341, 668],
                  [platforms.RED_MIDDLE, 1341, 643],
                  [platforms.RED_MIDDLE, 1341, 618],
                  [platforms.RED_MIDDLE, 1341, 593],
                  [platforms.RED_MIDDLE, 1341, 568],
                  [platforms.RED_MIDDLE, 1341, 543],
                  [platforms.RED_MIDDLE, 1341, 518],
                  [platforms.RED_MIDDLE, 1341, 493],
                  [platforms.RED_MIDDLE, 1341, 468],
                  [platforms.RED_MIDDLE, 1341, 443],
                  [platforms.RED_MIDDLE, 1341, 418],
                  [platforms.RED_MIDDLE, 1341, 393],
                  [platforms.RED_MIDDLE, 1341, 368],
                  [platforms.RED_MIDDLE, 1341, 343],
                  [platforms.RED_MIDDLE, 1341, 318],
                  [platforms.RED_MIDDLE, 1341, 293],
                  [platforms.RED_MIDDLE, 1341, 268],
                  [platforms.RED_MIDDLE, 1341, 243],
                  [platforms.RED_MIDDLE, 1341, 218],
                  [platforms.RED_MIDDLE, 1341, 193],
                  [platforms.RED_MIDDLE, 1341, 168],
                  [platforms.RED_MIDDLE, 1341, 143],
                  [platforms.RED_MIDDLE, 1341, 118],
                  [platforms.RED_MIDDLE, 1341, 93],
                  [platforms.RED_MIDDLE, 1341, 68],
                  [platforms.RED_MIDDLE, 1341, 43],
                  [platforms.RED_MIDDLE, 1341, 18],
                  [platforms.RED_MIDDLE, 1341, -7],

                  #Left Border
                  [platforms.RED_MIDDLE, 0, 743],
                  [platforms.RED_MIDDLE, 0, 718],
                  [platforms.RED_MIDDLE, 0, 693],
                  [platforms.RED_MIDDLE, 0, 668],
                  [platforms.RED_MIDDLE, 0, 643],
                  [platforms.RED_MIDDLE, 0, 618],
                  [platforms.RED_MIDDLE, 0, 593],
                  [platforms.RED_MIDDLE, 0, 568],
                  [platforms.RED_MIDDLE, 0, 543],
                  [platforms.RED_MIDDLE, 0, 518],
                  [platforms.RED_MIDDLE, 0, 493],
                  [platforms.RED_MIDDLE, 0, 468],
                  [platforms.RED_MIDDLE, 0, 443],
                  [platforms.RED_MIDDLE, 0, 418],
                  [platforms.RED_MIDDLE, 0, 393],
                  [platforms.RED_MIDDLE, 0, 368],
                  [platforms.RED_MIDDLE, 0, 343],
                  [platforms.RED_MIDDLE, 0, 318],
                  [platforms.RED_MIDDLE, 0, 293],
                  [platforms.RED_MIDDLE, 0, 268],
                  [platforms.RED_MIDDLE, 0, 243],
                  [platforms.RED_MIDDLE, 0, 218],
                  [platforms.RED_MIDDLE, 0, 193],
                  [platforms.RED_MIDDLE, 0, 168],
                  [platforms.RED_MIDDLE, 0, 143],
                  [platforms.RED_MIDDLE, 0, 118],
                  [platforms.RED_MIDDLE, 0, 93],
                  [platforms.RED_MIDDLE, 0, 68],
                  [platforms.RED_MIDDLE, 0, 43],
                  [platforms.RED_MIDDLE, 0, 18],
                  [platforms.RED_MIDDLE, 0, -7],

                  #Top Border
                  [platforms.RED_MIDDLE, -9, 0],
                  [platforms.RED_MIDDLE, 16, 0],
                  [platforms.RED_MIDDLE, 41, 0],
                  [platforms.RED_MIDDLE, 66, 0],
                  [platforms.RED_MIDDLE, 91, 0],
                  [platforms.RED_MIDDLE, 116, 0],
                  [platforms.RED_MIDDLE, 141, 0],
                  [platforms.RED_MIDDLE, 166, 0],
                  [platforms.RED_MIDDLE, 191, 0],
                  [platforms.RED_MIDDLE, 216, 0],
                  [platforms.RED_MIDDLE, 241, 0],
                  [platforms.RED_MIDDLE, 266, 0],
                  [platforms.RED_MIDDLE, 291, 0],
                  [platforms.RED_MIDDLE, 316, 0],
                  [platforms.RED_MIDDLE, 341, 0],
                  [platforms.RED_MIDDLE, 366, 0],
                  [platforms.RED_MIDDLE, 391, 0],
                  [platforms.RED_MIDDLE, 416, 0],
                  [platforms.RED_MIDDLE, 441, 0],
                  [platforms.RED_MIDDLE, 466, 0],
                  [platforms.RED_MIDDLE, 491, 0],
                  [platforms.RED_MIDDLE, 516, 0],
                  [platforms.RED_MIDDLE, 541, 0],
                  [platforms.RED_MIDDLE, 566, 0],
                  [platforms.RED_MIDDLE, 591, 0],
                  [platforms.RED_MIDDLE, 616, 0],
                  [platforms.RED_MIDDLE, 641, 0],
                  [platforms.RED_MIDDLE, 666, 0],
                  [platforms.RED_MIDDLE, 691, 0],
                  [platforms.RED_MIDDLE, 716, 0],
                  [platforms.RED_MIDDLE, 741, 0],
                  [platforms.RED_MIDDLE, 766, 0],
                  [platforms.RED_MIDDLE, 791, 0],
                  [platforms.RED_MIDDLE, 816, 0],
                  [platforms.RED_MIDDLE, 841, 0],
                  [platforms.RED_MIDDLE, 866, 0],
                  [platforms.RED_MIDDLE, 891, 0],
                  [platforms.RED_MIDDLE, 916, 0],
                  [platforms.RED_MIDDLE, 941, 0],
                  [platforms.RED_MIDDLE, 966, 0],
                  [platforms.RED_MIDDLE, 991, 0],
                  [platforms.RED_MIDDLE, 1016, 0],
                  [platforms.RED_MIDDLE, 1041, 0],
                  [platforms.RED_MIDDLE, 1066, 0],
                  [platforms.RED_MIDDLE, 1091, 0],
                  [platforms.RED_MIDDLE, 1116, 0],
                  [platforms.RED_MIDDLE, 1141, 0],
                  [platforms.RED_MIDDLE, 1166, 0],
                  [platforms.RED_MIDDLE, 1191, 0],
                  [platforms.RED_MIDDLE, 1216, 0],
                  [platforms.RED_MIDDLE, 1241, 0],
                  [platforms.RED_MIDDLE, 1266, 0],
                  [platforms.RED_MIDDLE, 1291, 0],
                  [platforms.RED_MIDDLE, 1316, 0],
                  [platforms.RED_MIDDLE, 1341, 0],

                  #Left Stairs Step 1
                  [platforms.RED_MIDDLE, 141, 718],
                  [platforms.RED_MIDDLE, 166, 718],
                  [platforms.RED_MIDDLE, 191, 718],
                  [platforms.RED_MIDDLE, 216, 718],
                  [platforms.RED_MIDDLE, 241, 718],
                  [platforms.RED_MIDDLE, 266, 718],
                  [platforms.RED_MIDDLE, 291, 718],
                  [platforms.RED_MIDDLE, 316, 718],
                  [platforms.RED_MIDDLE, 341, 718],
                  [platforms.RED_MIDDLE, 366, 718],
                  [platforms.RED_MIDDLE, 391, 718],
                  [platforms.RED_MIDDLE, 416, 718],
                  [platforms.RED_MIDDLE, 441, 718],
                  [platforms.RED_MIDDLE, 466, 718],
                  [platforms.RED_MIDDLE, 491, 718],
                  [platforms.RED_MIDDLE, 516, 718],
                  [platforms.RED_MIDDLE, 541, 718],
                  [platforms.RED_MIDDLE, 566, 718],
                  [platforms.RED_MIDDLE, 591, 718],
                  [platforms.RED_MIDDLE, 616, 718],
                  [platforms.RED_MIDDLE, 641, 718],
                  [platforms.RED_MIDDLE, 666, 718],
                  [platforms.RED_MIDDLE, 691, 718],
                  [platforms.RED_MIDDLE, 716, 718],
                  [platforms.RED_MIDDLE, 741, 718],
                  [platforms.RED_MIDDLE, 766, 718],
  
                  
                  #Left Stairs Step 2
                  [platforms.RED_MIDDLE, 166, 693],
                  [platforms.RED_MIDDLE, 191, 693],
                  [platforms.RED_MIDDLE, 216, 693],
                  [platforms.RED_MIDDLE, 241, 693],
                  [platforms.RED_MIDDLE, 266, 693],
                  [platforms.RED_MIDDLE, 291, 693],
                  [platforms.RED_MIDDLE, 316, 693],
                  [platforms.RED_MIDDLE, 341, 693],
                  
                  #Left Stairs Step 3
                  [platforms.RED_MIDDLE, 191, 668],
                  [platforms.RED_MIDDLE, 216, 668],
                  [platforms.RED_MIDDLE, 241, 668],
                  [platforms.RED_MIDDLE, 266, 668],
                  [platforms.RED_MIDDLE, 291, 668],

                  #Left Stairs Step 4
                  [platforms.RED_MIDDLE, 216, 643],
                  [platforms.RED_MIDDLE, 241, 643],
                  [platforms.RED_MIDDLE, 266, 643],
                  [platforms.RED_MIDDLE, 291, 643],

                  #Left Stairs Step 5
                  [platforms.RED_MIDDLE, 241, 618],
                  [platforms.RED_MIDDLE, 266, 618],
                  [platforms.RED_MIDDLE, 291, 618],

                  #Right AI Base Spot and pillar
                  [platforms.RED_MIDDLE, 1166, 718],
                  [platforms.RED_MIDDLE, 1166, 693],
                  [platforms.RED_MIDDLE, 1166, 668],
                  [platforms.RED_MIDDLE, 1166, 643],
                  [platforms.RED_MIDDLE, 1166, 618],
                  [platforms.RED_MIDDLE, 1166, 593],
                  [platforms.RED_MIDDLE, 1166, 568],
                  [platforms.RED_MIDDLE, 1166, 543],
                  [platforms.RED_MIDDLE, 1166, 518],
                  [platforms.RED_MIDDLE, 1166, 493],
                  [platforms.RED_MIDDLE, 1166, 468],
                  [platforms.RED_MIDDLE, 1166, 443],
                  
                  [platforms.RED_MIDDLE, 1191, 718],
                  [platforms.RED_MIDDLE, 1191, 693],
                  [platforms.RED_MIDDLE, 1191, 668],
                  [platforms.RED_MIDDLE, 1191, 643],
                  [platforms.RED_MIDDLE, 1191, 618],
                  [platforms.RED_MIDDLE, 1191, 593],
                  [platforms.RED_MIDDLE, 1191, 568],
                  [platforms.RED_MIDDLE, 1191, 543],
                  [platforms.RED_MIDDLE, 1191, 518],
                  [platforms.RED_MIDDLE, 1191, 493],
                  [platforms.RED_MIDDLE, 1191, 468],
                  [platforms.RED_MIDDLE, 1191, 443],

                  #Jumping platforms
                  
                  [platforms.RED_MIDDLE, 1216, 668],

                  [platforms.RED_MIDDLE, 1316, 593],

                  [platforms.RED_MIDDLE, 1216, 518],

                  


                  [platforms.RED_MIDDLE, 866, 718],
                  [platforms.RED_MIDDLE, 891, 718],
                  [platforms.RED_MIDDLE, 916, 718],
                  [platforms.RED_MIDDLE, 941, 718],
                  [platforms.RED_MIDDLE, 966, 718],
                  [platforms.RED_MIDDLE, 991, 718],
                  [platforms.RED_MIDDLE, 1016, 718],
                  [platforms.RED_MIDDLE, 1041, 718],
                  [platforms.RED_MIDDLE, 1066, 718],
                  [platforms.RED_MIDDLE, 1091, 718],
                  [platforms.RED_MIDDLE, 1116, 718],
                  [platforms.RED_MIDDLE, 1141, 718],
                  [platforms.RED_MIDDLE, 1091, 593],
                  [platforms.RED_MIDDLE, 1116, 593],
                  [platforms.RED_MIDDLE, 1141, 593],
                  [platforms.RED_MIDDLE, 1091, 568],
                  [platforms.RED_MIDDLE, 1116, 568],
                  [platforms.RED_MIDDLE, 1141, 568],
                  [platforms.RED_MIDDLE, 1091, 543],
                  [platforms.RED_MIDDLE, 1116, 543],
                  [platforms.RED_MIDDLE, 1141, 543],
                  [platforms.RED_MIDDLE, 1091, 518],
                  [platforms.RED_MIDDLE, 1116, 518],
                  [platforms.RED_MIDDLE, 1141, 518],
                  [platforms.RED_MIDDLE, 1091, 493],
                  [platforms.RED_MIDDLE, 1116, 493],
                  [platforms.RED_MIDDLE, 1141, 493],
                  [platforms.RED_MIDDLE, 1091, 468],
                  [platforms.RED_MIDDLE, 1116, 468],
                  [platforms.RED_MIDDLE, 1141, 468],
                  [platforms.RED_MIDDLE, 1091, 443],
                  [platforms.RED_MIDDLE, 1116, 443],
                  [platforms.RED_MIDDLE, 1141, 443],


                  [platforms.RED_MIDDLE, 1066, 593],
                  [platforms.RED_MIDDLE, 1066, 568],
                  [platforms.RED_MIDDLE, 1066, 543],
                  [platforms.RED_MIDDLE, 1066, 518],
                  [platforms.RED_MIDDLE, 1066, 493],
                  [platforms.RED_MIDDLE, 1066, 468],
                  [platforms.RED_MIDDLE, 1066, 443],

                  #First upper platform

                  [platforms.RED_MIDDLE, 891, 368],
                  [platforms.RED_MIDDLE, 891, 343],
                  [platforms.RED_MIDDLE, 866, 368],
                  [platforms.RED_MIDDLE, 866, 343],
                  [platforms.RED_MIDDLE, 841, 368],
                  [platforms.RED_MIDDLE, 841, 343],
                  [platforms.RED_MIDDLE, 816, 368],
                  [platforms.RED_MIDDLE, 816, 343],
                  [platforms.RED_MIDDLE, 791, 368],
                  [platforms.RED_MIDDLE, 791, 343],
                  [platforms.RED_MIDDLE, 766, 368],
                  [platforms.RED_MIDDLE, 766, 343],
                  [platforms.RED_MIDDLE, 741, 368],
                  [platforms.RED_MIDDLE, 741, 343],
                  [platforms.RED_MIDDLE, 716, 368],
                  [platforms.RED_MIDDLE, 716, 343],
                  [platforms.RED_MIDDLE, 691, 368],
                  [platforms.RED_MIDDLE, 691, 343],
                  [platforms.RED_MIDDLE, 666, 368],
                  [platforms.RED_MIDDLE, 666, 343],
                  [platforms.RED_MIDDLE, 641, 368],
                  [platforms.RED_MIDDLE, 641, 343],

                  #Gap is above here
                  [platforms.RED_MIDDLE, 616, 368],
                  [platforms.RED_MIDDLE, 616, 343],
                  [platforms.RED_MIDDLE, 616, 318],
                  [platforms.RED_MIDDLE, 591, 368],
                  [platforms.RED_MIDDLE, 591, 343],
                  [platforms.RED_MIDDLE, 591, 318],
                  [platforms.RED_MIDDLE, 591, 293],
                  [platforms.RED_MIDDLE, 566, 368],
                  [platforms.RED_MIDDLE, 566, 343],
                  [platforms.RED_MIDDLE, 566, 318],
                  
                  [platforms.RED_MIDDLE, 541, 368],
                  [platforms.RED_MIDDLE, 541, 343],
                  [platforms.RED_MIDDLE, 516, 368],
                  [platforms.RED_MIDDLE, 516, 343],
                  [platforms.RED_MIDDLE, 491, 368],
                  [platforms.RED_MIDDLE, 491, 343],
                  [platforms.RED_MIDDLE, 466, 368],
                  [platforms.RED_MIDDLE, 466, 343],
                  [platforms.RED_MIDDLE, 441, 368],
                  [platforms.RED_MIDDLE, 441, 343],
                  [platforms.RED_MIDDLE, 416, 368],
                  [platforms.RED_MIDDLE, 416, 343],
                  [platforms.RED_MIDDLE, 391, 368],
                  [platforms.RED_MIDDLE, 391, 343],
                  [platforms.RED_MIDDLE, 366, 368],
                  [platforms.RED_MIDDLE, 366, 343],
                  [platforms.RED_MIDDLE, 341, 368],
                  [platforms.RED_MIDDLE, 341, 343],
                  [platforms.RED_MIDDLE, 316, 368],
                  [platforms.RED_MIDDLE, 316, 343],
                  [platforms.RED_MIDDLE, 291, 368],
                  [platforms.RED_MIDDLE, 291, 343],
                  [platforms.RED_MIDDLE, 266, 368],
                  [platforms.RED_MIDDLE, 266, 343],
                  [platforms.RED_MIDDLE, 241, 368],
                  [platforms.RED_MIDDLE, 241, 343],

                  #Second upper platform
                  [platforms.RED_MIDDLE, 866, 218],
                  [platforms.RED_MIDDLE, 891, 218],
                  [platforms.RED_MIDDLE, 841, 218],
                  [platforms.RED_MIDDLE, 816, 218],
                  [platforms.RED_MIDDLE, 791, 218],
                  [platforms.RED_MIDDLE, 766, 218],
                  [platforms.RED_MIDDLE, 741, 218],
                  [platforms.RED_MIDDLE, 716, 218],
                  [platforms.RED_MIDDLE, 691, 218],
                  [platforms.RED_MIDDLE, 491, 218],
                  [platforms.RED_MIDDLE, 466, 218],
                  [platforms.RED_MIDDLE, 441, 218],
                  [platforms.RED_MIDDLE, 416, 218],
                  [platforms.RED_MIDDLE, 391, 218],
                  
                  #Gap is above here
                  [platforms.RED_MIDDLE, 366, 193],
                  [platforms.RED_MIDDLE, 366, 218],
                  [platforms.RED_MIDDLE, 341, 218],
                  [platforms.RED_MIDDLE, 341, 168],
                  [platforms.RED_MIDDLE, 341, 193],
                  [platforms.RED_MIDDLE, 316, 218],
                  [platforms.RED_MIDDLE, 316, 193],
                  [platforms.RED_MIDDLE, 291, 218],
                  [platforms.RED_MIDDLE, 266, 218],
                  [platforms.RED_MIDDLE, 241, 218],
                  [platforms.RED_MIDDLE, 141, 218],
                  [platforms.RED_MIDDLE, 166, 218],
                  [platforms.RED_MIDDLE, 191, 218],
                  [platforms.RED_MIDDLE, 216, 218],

                  #Third Upper platform

                  [platforms.RED_MIDDLE, 16, 91],
                  [platforms.RED_MIDDLE, 41, 91],
                  [platforms.RED_MIDDLE, 66, 91],
                  [platforms.RED_MIDDLE, 91, 91],
                  [platforms.RED_MIDDLE, 116, 91],
                  [platforms.RED_MIDDLE, 141, 91],
                  [platforms.RED_MIDDLE, 166, 91],
                  [platforms.RED_MIDDLE, 191, 91],
                  [platforms.RED_MIDDLE, 216, 91],
                  [platforms.RED_MIDDLE, 241, 91],

                  [platforms.RED_MIDDLE, 491, 91],
                  [platforms.RED_MIDDLE, 516, 91],
                  [platforms.RED_MIDDLE, 541, 91],
                  [platforms.RED_MIDDLE, 566, 91],
                  [platforms.RED_MIDDLE, 591, 91],
                  [platforms.RED_MIDDLE, 616, 91],
                  [platforms.RED_MIDDLE, 641, 91],
                  [platforms.RED_MIDDLE, 666, 91],
                  [platforms.RED_MIDDLE, 691, 91],
                  [platforms.RED_MIDDLE, 716, 91],
                  [platforms.RED_MIDDLE, 741, 91],
                  [platforms.RED_MIDDLE, 766, 91],
                  [platforms.RED_MIDDLE, 791, 91],
                  [platforms.RED_MIDDLE, 816, 91],
                  [platforms.RED_MIDDLE, 841, 91],
                  [platforms.RED_MIDDLE, 866, 91],
                  [platforms.RED_MIDDLE, 891, 91],
                  [platforms.RED_MIDDLE, 916, 91],
                  [platforms.RED_MIDDLE, 941, 91],
                  [platforms.RED_MIDDLE, 966, 91],
                  [platforms.RED_MIDDLE, 991, 91],
                  [platforms.RED_MIDDLE, 1016, 91],
                  [platforms.RED_MIDDLE, 1041, 91],
                  [platforms.RED_MIDDLE, 1066, 91],
                  [platforms.RED_MIDDLE, 1091, 91],
                  [platforms.RED_MIDDLE, 1116, 91],
                  [platforms.RED_MIDDLE, 1141, 91],
                  [platforms.RED_MIDDLE, 1166, 91],
                  [platforms.RED_MIDDLE, 1191, 91],
                  [platforms.RED_MIDDLE, 1216, 91],
                  [platforms.RED_MIDDLE, 1241, 91],
                  [platforms.RED_MIDDLE, 1266, 91],
                  [platforms.RED_MIDDLE, 1291, 91],
                  [platforms.RED_MIDDLE, 1316, 91],
                  [platforms.RED_MIDDLE, 1341, 91],





                  [platforms.RED_MIDDLE, 1016, 216],
                  [platforms.RED_MIDDLE, 1041, 216],
                  [platforms.RED_MIDDLE, 1066, 216],
                  [platforms.RED_MIDDLE, 1091, 216],
                  [platforms.RED_MIDDLE, 1116, 216],
                  [platforms.RED_MIDDLE, 1141, 216],
                  [platforms.RED_MIDDLE, 1166, 216],
                  [platforms.RED_MIDDLE, 1191, 216],
                  [platforms.RED_MIDDLE, 1216, 216],
                  [platforms.RED_MIDDLE, 1241, 216],
                  [platforms.RED_MIDDLE, 1266, 216],
                  [platforms.RED_MIDDLE, 1291, 216],
                  [platforms.RED_MIDDLE, 1316, 216],
                  [platforms.RED_MIDDLE, 1341, 216],


                  [platforms.RED_MIDDLE, 1066, 341],
                  [platforms.RED_MIDDLE, 1091, 341],
                  [platforms.RED_MIDDLE, 1116, 341],
                  [platforms.RED_MIDDLE, 1141, 341],
                  [platforms.RED_MIDDLE, 1166, 341],
                  [platforms.RED_MIDDLE, 1191, 341],
                  [platforms.RED_MIDDLE, 1216, 341],
                  [platforms.RED_MIDDLE, 1241, 341],
                  [platforms.RED_MIDDLE, 1266, 341],
                  [platforms.RED_MIDDLE, 1291, 341],
                  [platforms.RED_MIDDLE, 1316, 341],
                  [platforms.RED_MIDDLE, 1341, 341],


                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
        #First horizontal platform

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 425
        block.rect.y = 545
        block.boundary_left = 350
        block.boundary_right = 530
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        #Second horizontal platform

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 670
        block.rect.y = 545
        block.boundary_left = 570
        block.boundary_right = 850
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Raccoon

        block = platforms.MovingPlatform(platforms.RACCOON)
        block.rect.x = 1000
        block.rect.y = 698
        block.boundary_left = 880
        block.boundary_right = 1040
        block.change_x = 13
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #second vertical platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 968
        block.rect.y = 500
        block.boundary_top = 380
        block.boundary_bottom = 610
        block.change_y = 5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Beginning vertical platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 66
        block.rect.y = 500
        block.boundary_top = 380
        block.boundary_bottom = 618
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



