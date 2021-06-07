from test import Enemy
import pygame

# Import random for random numbers
import random
import pathlib
path = pathlib.Path(__file__).parent.absolute()
print(path)
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1920//3
SCREEN_HEIGHT = 1000
import time


clock = pygame.time.Clock()

class Particule(pygame.sprite.Sprite):
    def __init__(self,rectBottom,rectLeft):
        import os.path
        num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
        super(Particule, self).__init__()
        self.motion = [pygame.image.load("attacks/explosion_1/frame_0.png"),pygame.image.load("attacks/explosion_1/frame_1.png"),pygame.image.load("attacks/explosion_1/frame_2.png"),pygame.image.load("attacks/explosion_1/frame_3.png"),pygame.image.load("attacks/explosion_1/frame_4.png"),pygame.image.load("attacks/explosion_1/frame_5.png"),pygame.image.load("attacks/explosion_1/frame_6.png")]
        for x in  range(num_files):
            pygame.image.load("attacks/explosion_1/frame_0.png")
            
          

        self.surf =self.motion[0]
        self.rect = self.surf.get_rect()
        self.rect.bottom = rectBottom
        self.rect.left = rectLeft
        self.cooldown = 100
        self.lastAnimation= 0
        self.animNum = 0
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.lastAnimation >= self.cooldown:
            self.lastAnimation = pygame.time.get_ticks()
            
            if 6>=self.animNum :
                
                
                self.surf = self.motion[self.animNum]
                self.animNum += 1
            else:
                self.animNum = 0
                self.kill()
            
            
           

                





class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        
        self.surf = pygame.image.load(f"{path}\Ships\Ship_1.png").convert_alpha()
        self.score = 0
        self.rect = self.surf.get_rect()
        self.lastBullet= 0
        self.cooldown = 100
        self.life = 200
        self.maxLife = 200

    # Move the sprite based on keypresses
    def update(self,mousePos):
        global running
        self.rect.left = mousePos[0] -75//2
        self.rect.bottom = 900
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


        if pygame.sprite.spritecollideany(self, bullet):
            CollidedBullet = pygame.sprite.spritecollideany(self, bullet)
            if CollidedBullet.ally == False:

                self.life -= CollidedBullet.damage
                CollidedBullet.kill()
                
                if self.life <= 0:
                    self.kill()
                    running = False
        self.size = self.surf.get_size()
        
    def fire(self ,mousePos,isSuper ):
        now = pygame.time.get_ticks()
        if now - self.lastBullet >= self.cooldown:
            self.lastBullet = pygame.time.get_ticks()
            bul = Bullet(True,isSuper)
            if isSuper == 1 : 
                bul.rect.left = mousePos[0] -21
            elif isSuper ==0 :
                bul.rect.left = mousePos[0] -9
            bullet.add(bul)
            all_sprites.add(bul)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,ally,isSuper):
        super(Bullet, self).__init__()
        self.ally = ally
        if self.ally :
            if isSuper  == 0 : 
                self.surf = pygame.image.load("attacks/fire_1/Fire_1_3.png").convert_alpha()
                self.damage =10
            elif isSuper  == 1 :
                self.surf = pygame.image.load("attacks/Special_1/Special_1.png").convert_alpha()
                self.damage = 50
        else:
            self.surf = pygame.image.load("attacks/fire_2/Fire_1_3.png").convert_alpha()
            self.damage = 10

       
        self.rect = self.surf.get_rect()
        self.rect.bottom = 860
        self.rect.left = 0
        
        
        
        
    def update(self):
        if self.rect.bottom < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
        if self.ally :
            
            self.speed = 5
            self.rect.move_ip(0,-self.speed)
            
        else :
            
            self.speed = 3
            self.rect.move_ip(0,self.speed)


class Ennemy(pygame.sprite.Sprite):
    def __init__(self,EnemyType):
        super(Ennemy, self).__init__()
        if EnemyType == 1 :
            self.surf = pygame.image.load("Enemy/Enemy_1/ship/ship.png").convert_alpha()
            self.maxLife = 100
            self.life = 100
            self.cooldown = 2000
            self.typeEnemy= EnemyType
        elif EnemyType == 2 : 
            self.surf = pygame.image.load("Enemy/Enemy_2/ship/ship.png").convert_alpha()
            self.maxLife = 40
            self.life = 40
            self.cooldown = 1500
            self.typeEnemy= EnemyType
        self.lastBullet = 0
        self.rect = self.surf.get_rect()
        self.rect.left = random.randint(50,590)
        self.speed = 1
        
       
    def fire(self):
        now = pygame.time.get_ticks()
        if now - self.lastBullet >= self.cooldown:
            self.lastBullet = pygame.time.get_ticks()
            bul = Bullet(False, 0)
            if self.typeEnemy == 1 :
                bul.rect.left = self.rect.left +45
            elif self.typeEnemy == 2 :
                bul.rect.left = self.rect.left +20

            bul.rect.bottom = self.rect.bottom+9
            bullet.add(bul)
            all_sprites.add(bul)
    
    def update(self):
        
        self.rect.move_ip(0,self.speed)
        self.size = self.surf.get_size()
        pygame.draw.rect(screen, (0,255,0), (self.rect.left   , self.rect.bottom -self.size[1] -13,self.size[0] * (self.life / self.maxLife),10))
        self.fire()
        #pygame.draw.rect(screen, (0,255,0), (self.rect.left , self.rect.bottom , self.rect.left+1, self.rect.bottom ))

        
    
        if pygame.sprite.spritecollideany(self, bullet):
            CollidedBullet = pygame.sprite.spritecollideany(self, bullet)
            if CollidedBullet.ally == True:
                
                self.life -= CollidedBullet.damage
                CollidedBullet.kill()
                if self.life <= 0:
                    if self.typeEnemy == 1 :
                        player.score += 10
                    elif self.typeEnemy == 2 :
                        player.score += 5
                    par = Particule(self.rect.bottom, self.rect.left)
                    particule.add(par)
                    all_sprites.add(par)
                    self.kill()
                
class Map(pygame.sprite.Sprite):
    def __init__(self):
        super(Map, self).__init__()
        self.surf = pygame.image.load("Map/map_1.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.mapSpeed = 2

    def update(self):
        self.rect.move_ip(0 , self.mapSpeed)
        
    
def display():
    pygame.draw.rect(screen, (255,0,0), (20  , SCREEN_HEIGHT - 50, 400, 30))
    pygame.draw.rect(screen, (0,255,0), (20  , SCREEN_HEIGHT - 50, 400* (player.life / player.maxLife), 30))


    screen.blit(pixelFont.render("LIFE", True, (0,0,255)), (20 , SCREEN_HEIGHT - 85))  
    screen.blit(pixelFont.render(f"SCORE : {player.score}"  , True, (255,255,255)), (20 , 30))        


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player= Player()


bullet = pygame.sprite.Group()
ennemy = pygame.sprite.Group()
particule = pygame.sprite.Group()
map = pygame.sprite.Group()

map.add(Map())
all_sprites = pygame.sprite.Group()
all_sprites.add(map)
all_sprites.add(player)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 5000)
pixelFont = pygame.font.Font("font/Pixeboy.ttf", 50)

running=True
mouseIsDown= False
EIsDown = False
clock = pygame.time.Clock()
while running:
    #Verifie si l'événement close window a eu lieu
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseIsDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseIsDown = False
        elif event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_e:
                EIsDown= True
        elif event.type ==  pygame.KEYUP:
            if event.key == pygame.K_e:
                EIsDown= False
                
        elif event.type == ADDENEMY :
            for i in range(random.randint(1, 5)):
                en = Ennemy(random.randint(1,2))
                ennemy.add(en)
                
                all_sprites.add(en)

    if mouseIsDown == True :
        player.fire(mousePos, 0)

    elif EIsDown == True:
        player.fire(mousePos, 1)
   
    
    
    screen.fill((0,0,0))
    pressed_keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    
    player.update(mousePos)
    bullet.update()
    particule.update()
    ennemy.update()
    map.update()
    
    
    
    for entity in all_sprites:
        #mousePos = pygame.mouse.get_pos()
        #screen.blit(entity.surf, (mousePos[0] - 75//2, 900))
        screen.blit(entity.surf, entity.rect)
        
   
    display()
    pygame.display.flip()
    clock.tick(144)
