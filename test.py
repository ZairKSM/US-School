import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        
pygame.init()

screen = pygame.display.set_mode((640, 480))

background = pygame.Surface((640, 480))
background.fill((0, 0, 0))

player = Player()

state = 0
x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        

    mousePos = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    screen.blit(player.surf, (mousePos[0], 235))
    
    pygame.display.flip()

