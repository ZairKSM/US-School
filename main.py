import pygame
import pathlib
path = pathlib.Path(__file__).parent.absolute()
print(path)
"""from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)"""

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        
        self.surf = pygame.image.load(f"{path}\Ships\Ship_1.png").convert()
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

pygame.init()
SCREEN_WIDTH = 1920//3
SCREEN_HEIGHT = 1000

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill((0, 0, 0))

player = Player()
running = True
screen.blit(player.surf, (SCREEN_WIDTH/2- 75//2, SCREEN_HEIGHT*0.90))
while running:
    #Verifie si l'événement close window a eu lieu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed_keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    
    screen.blit(background, (0, 0))
    screen.blit(player.surf, (mousePos[0]- 75//2 , SCREEN_HEIGHT*0.85))
  
    pygame.display.flip()