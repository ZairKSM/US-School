import pygame
import sys
import pygame.sprite as sprite

theClock = pygame.time.Clock()

background = pygame.image.load('Map/map_3.png')

background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode((640,1000))
w,h = background_size
x = 0
y = 0

x1 = 0
y1 = -h

running = True

while running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    y1 += 20
    y += 20
    screen.blit(background,(0,y))
    screen.blit(background,(0,y1))
    if y > h:
        y = -h
    if y1 > h:
        y1 = -h
    pygame.display.flip()
    pygame.display.update()
    theClock.tick(144)