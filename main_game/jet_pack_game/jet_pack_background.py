import pygame
from jet_pack_constants import *

class MainBackground:
    """Establishes main background for jetpack game, want jetpack background to be moving with the obstacles"""

    def __init__(self):
        super(MainBackground, self).__init__()
        #self.surf = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create the surface that is the football field
        surface = pygame.image.load(WHITE_BACKGROUND).convert()
        self.surf = pygame.transform.scale(surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.x = 0
        self.y = 0
        
        # Move at the speed set in the constants file
        self.speed = 0
        

            
    def render(self, screen):
        # We can have a render method here since its not gonna be in the sprite group
        screen.blit(self.surf, (self.x, self.y))