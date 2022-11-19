import math
import random 

import pygame 
from pygame.locals import *

from jet_pack_constants import *


class JetPacker(pygame.sprite.Sprite):
    """Operation to control JetPack boy"""
    def __init__(self):
        super(JetPacker, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()


    def update(self, key_press) -> None:
        # Space down function
        if key_press[KEYUP]:
            self.rect.move_ip(0, -50)
        if key_press[KEYDOWN]:
            self.rect.move_ip(0, 50)

        # Checks if jetpacker is hitting bounds
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT     


                