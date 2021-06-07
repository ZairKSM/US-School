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
        self.score = 160
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
        self.super= isSuper
        if self.ally :
            if isSuper  == 0 : 
                self.surf = pygame.image.load("attacks/fire_1/Fire_1_3.png").convert_alpha()
                self.damage =10
            elif isSuper  == 1 :
                self.surf = pygame.image.load("attacks/Special_1/Special_1.png").convert_alpha()
                self.damage = 50
        else:
            if isSuper == 3:
                self.surf = pygame.image.load("attacks/Special_2/Special_2.png").convert_alpha()
                self.damage = 20

            
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
            if self.super == 3:
                self.speed = 10
                self.rect.move_ip(0,self.speed)
            else:
                self.speed = 3
                self.rect.move_ip(0,self.speed)


class Ennemy(pygame.sprite.Sprite):
    def __init__(self,EnemyType):
        super(Ennemy, self).__init__()
        if EnemyType == 1 :
            self.surf = pygame.image.load("Enemy/Enemy_1/ship/ship.png").convert_alpha()
            self.rect = self.surf.get_rect()
            self.rect.left = random.randint(50,590)
            self.maxLife = 100
            self.life = 100
            self.cooldown = 2000
            self.typeEnemy= EnemyType
            self.speed = 1
        elif EnemyType == 2 : 
            self.surf = pygame.image.load("Enemy/Enemy_2/ship/ship.png").convert_alpha()
            self.rect = self.surf.get_rect()
            self.rect.left = random.randint(50,590)
            self.maxLife = 40
            self.life = 40
            self.cooldown = 1000
            self.typeEnemy= EnemyType
            self.speed = 2
        elif EnemyType == 3 : 
            self.surf = pygame.image.load("Enemy/Enemy_3/ship/ship.png").convert_alpha()
            self.rect = self.surf.get_rect()
            self.rect.left = random.randint(50,590)
            self.maxLife = 20
            self.life = 20
            self.cooldown = 1000
            self.typeEnemy= EnemyType
            self.speed = 2
        elif EnemyType == 4 : 
            self.surf = pygame.image.load("Enemy/Boss_1/ship.png").convert_alpha()
            self.surf =  pygame.transform.scale(self.surf, (int(72*2.5), int(73*2.5)))
            self.rect = self.surf.get_rect()
            self.rect.left = random.randint(0,450)
            self.maxLife = 1500
            self.life = 1500
            self.cooldown = 300
            self.typeEnemy= EnemyType
            self.speed = 2
            self.wall = False
        elif EnemyType == 5 : 
            self.surf = pygame.image.load("Enemy/Boss_2/ship.png").convert_alpha()
            self.surf =  pygame.transform.scale(self.surf, (int(72*2.5), int(73*2.5)))
            self.rect = self.surf.get_rect()
            self.rect.left = random.randint(0,450)
            self.maxLife = 1500
            self.life = 1500
            self.cooldown = 700
            self.typeEnemy= EnemyType
            self.speed = 2
            self.wall = False
            
        self.lastBullet = 0
        
        self.rect.bottom = -100
        
        
       
    def fire(self):
        now = pygame.time.get_ticks()
        if now - self.lastBullet >= self.cooldown:
            self.lastBullet = pygame.time.get_ticks()
            
            if self.typeEnemy == 1 :
                bul = Bullet(False, 0)
                bul.rect.left = self.rect.left +45
            elif self.typeEnemy == 2 :
                bul = Bullet(False, 0)
                bul.rect.left = self.rect.left +20
            elif self.typeEnemy == 3 :
                bul = Bullet(False, 0)
                bul.rect.left = self.rect.left +20
            elif self.typeEnemy == 4 :
                bul = Bullet(False, 0)
                bul.rect.left = self.rect.left +85
            elif self.typeEnemy == 5 :
                bul = Bullet(False, 3)
                bul.rect.left = self.rect.left +75

            bul.rect.bottom = self.rect.bottom+9
            bullet.add(bul)
            all_sprites.add(bul)
    
    def update(self):
        if self.typeEnemy == 4 or self.typeEnemy == 5 :
            if self.rect.bottom < 350:
                self.rect.move_ip(0,self.speed)

            elif self.rect.left < 450 and not(self.wall):
                    self.rect.move_ip(self.speed,0)
            elif self.rect.left > 0 :
                self.wall = True
                self.rect.move_ip(-self.speed,0)
            else : 
                self.wall = False

            
            
            
            
        

            self.size = self.surf.get_size()
            pygame.draw.rect(screen, (0,255,0), (self.rect.left   , self.rect.bottom -self.size[1] -13,self.size[0] * (self.life / self.maxLife),10))
            self.fire()

        else:
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
                    elif self.typeEnemy == 3 :
                        player.score += 15
                    elif self.typeEnemy == 4 or self.typeEnemy == 5:
                        player.score += 200
                        global combatBoss
                        combatBoss = False
                    
                    par = Particule(self.rect.bottom, self.rect.left)
                    particule.add(par)
                    all_sprites.add(par)
                    self.kill()



            

        
            
            
        

            
      
            
def display():
    pygame.draw.rect(screen, (255,0,0), (20  , SCREEN_HEIGHT - 50, 400, 30))
    pygame.draw.rect(screen, (0,255,0), (20  , SCREEN_HEIGHT - 50, 400* (player.life / player.maxLife), 30))


    screen.blit(pixelFont.render("LIFE", True, (0,0,255)), (20 , SCREEN_HEIGHT - 85))  
    screen.blit(pixelFont.render(f"SCORE : {player.score}"  , True, (255,255,255)), (20 , 30))        


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Mapsurf = pygame.image.load(f"Map/map_3.png").convert_alpha()
y = -8192     
y1 = 0
def update():
    global y
    global y1
    global surf
    
    y1 += 5
    y += 5
    screen.blit( Mapsurf,(0,y))
    screen.blit( Mapsurf,(0,y1))
    if y > 8192:
        y = -8190
    if y1 > 8192:
        y1 = -8190
player= Player()


bullet = pygame.sprite.Group()
ennemy = pygame.sprite.Group()
particule = pygame.sprite.Group()




all_sprites = pygame.sprite.Group()
all_sprites.add(player)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 5000)
ADDBOSS = pygame.USEREVENT + 2
pygame.time.set_timer(ADDBOSS, 10000)
pixelFont = pygame.font.Font("font/Pixeboy.ttf", 50)

running=True
mouseIsDown= False
EIsDown = False
clock = pygame.time.Clock()
combatBoss = False
k=0
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
                en = Ennemy(random.randint(1,3))
                ennemy.add(en)
                
                all_sprites.add(en)
        
        elif event.type == ADDBOSS:
            if player.score >= 50:
                if combatBoss == False:
                    k+=1
                    print(combatBoss)
                    combatBoss=True
                    if k%2 ==1 :
                        n=4
                    else: n = 5
                    en=  Ennemy(n)
                    ennemy.add(en)   
                    all_sprites.add(en)
                    

    if mouseIsDown == True :
        player.fire(mousePos, 0)

    elif EIsDown == True:
        player.fire(mousePos, 1)
   
    
    
    screen.fill((0,0,0))
    pressed_keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    update()
    player.update(mousePos)
    bullet.update()
    particule.update()
    ennemy.update()
    
    
    
    for entity in all_sprites:
        #mousePos = pygame.mouse.get_pos()
        #screen.blit(entity.surf, (mousePos[0] - 75//2, 900))
        screen.blit(entity.surf, entity.rect)
        
   
    display()
    pygame.display.flip()
    clock.tick(144)
