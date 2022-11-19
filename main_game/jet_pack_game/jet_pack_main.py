# Importing all modules
import pygame, random
from pygame.locals import KEYDOWN, QUIT
from jet_pack_characters import *
from jet_pack_constants import *
from jet_pack_background import *

# Use of different Classes



class square:
    rect: pygame.Rect
    color: tuple

    def __init__(self, rect) -> None:
        self.rect = rect
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    def fall(self):
        self.rect.move_ip(0, 1)
        if self.rect.bottom == 600:
            self.rect.bottom = random.randint(-1000, 0)
            self.rect.x = random.randint(100, 470)

def main():
    """The game."""
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


    jetpacker = JetPacker()
    background = MainBackground()
    zappers = [square(pygame.Rect(random.randint(100, 290), random.randint(-1000, 0), random.randint(10, 20), random.randint(10, 30))) for i in range(10)]
    clock = pygame.time.Clock()

    is_true  = True
    while is_true:
        for event in pygame.event.get():
            # Stop loop when X button is hit
            if event.type == QUIT:
                is_true = False
                
        key_press = pygame.key.get_pressed()

        jetpacker.update(key_press)

        background.render(screen)
        # pygame.draw.rect(main_screen, player.color, player.rect)
        screen.blit(jetpacker.surf, jetpacker.rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()