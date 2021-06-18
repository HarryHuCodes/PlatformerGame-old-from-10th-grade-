import pygame
import platforms
from spritesheet_functions import SpriteSheet

class Ball(pygame.sprite.Sprite):
    
    def __init__(self):

        #Extends parent's constructor
        super().__init__()
        
        #Create sprite lists
##        self.glowing_frames = []
##        self.fading_frames = []
##        self.igniting_frames = []
        
        

        sprite_sheet = SpriteSheet("singleball.png")
        self.image = sprite_sheet.get_image(0, 3, 45, 40)

        #Set glowing animation 
        #self.image = sprite_sheet.get_image(353, 1, 30, 31)
        #self.glowing_frames.append(self.image)
        #self.image = sprite_sheet.get_image(350, 128, 34, 31)
        #self.glowing_frames.append(self.image)
        #self.image = sprite_sheet.get_image(159, 129, 33, 32)
        #self.glowing_frames.append(self.image)
        #self.image = sprite_sheet.get_image(159, 2, 33, 30)
        #self.glowing_frames.append(self.image)
        
        

        #Set fading animation
##        self.image = sprite_sheet.get_image(193, 36, 28, 25)
##        self.fading_frames.append(self.image)
##        self.image = sprite_sheet.get_image(192, 64, 31, 33)
##        self.fading_frames.append(self.image)
##        self.image = sprite_sheet.get_image(195, 97, 24, 27)
##        self.fading_frames.append(self.image)
##        self.image = sprite_sheet.get_image(292, 62, 22, 31)
##        self.fading_frames.append(self.image)

        #Set igniting animation
##        self.image = sprite_sheet.get_image(294, 7, 18, 18)
##        self.igniting_frames.append(self.image)
##        self.image = sprite_sheet.get_image(324, 5, 23, 23)
##        self.igniting_frames.append(self.image)
##        self.image = sprite_sheet.get_image(192, 1, 31, 31)
##        self.igniting_frames.append(self.image)

        self.rect = self.image.get_rect()

    
            
            
        
