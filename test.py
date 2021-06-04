import pygame, random, sys

def main():
  pygame.init()

  global screenSize, allColors, FPS, clock, surface

  screenSize = (640, 480)

  surface = pygame.display.set_mode(screenSize)
  pygame.display.set_caption('Space Shooters')

  black    = (0  , 0  , 0  )
  white    = (255, 255, 255)
  gray     = (100, 100, 100)
  navyblue = (60 , 60 , 100)
  red      = (255, 0  , 0  )
  green    = (0  , 255, 0  )
  blue     = (0  , 0  , 255)
  yellow   = (255, 255, 0  )
  orange   = (255, 155, 55 )
  purple   = (255, 0  , 255)
  cyan     = (0  , 255, 255)
  #             0      1     2      3      4      5       6      7       8       9
  allColors = [white,red, green, blue, yellow, orange, purple, cyan, navyblue, gray]
  clock = pygame.time.Clock()

  FPS = 64
#-------------------------------------------------------------------------------
  spaceship = Spaceship()
  bullets = Bullet(spaceship)
  while True:
    #step1 SetDelay
    clock.tick(FPS)
    #step2 reactOnPlayerInput
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        terminate()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          terminate()
        if event.key == pygame.K_UP:
          spaceship.moveUp = True
          spaceship.moveDown = False
        if event.key == pygame.K_DOWN:
          spaceship.moveUp = False
          spaceship.moveDown = True
        if event.key == pygame.K_LEFT:
          spaceship.moveRight = False
          spaceship.moveLeft = True
        if event.key == pygame.K_RIGHT:
          spaceship.moveRight = True
          spaceship.moveLeft = False
        if event.key == pygame.K_SPACE:
          bullets.isShooting = True

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          spaceship.moveUp = False
        if event.key == pygame.K_DOWN:
          spaceship.moveDown = False
        if event.key == pygame.K_LEFT:
          spaceship.moveLeft = False
        if event.key == pygame.K_RIGHT:
          spaceship.moveRight = False
        if event.key == pygame.K_SPACE:
          bullets.isShooting = False

    #step3 updateClasses/Variables
    spaceship.update()
    bullets.update(spaceship)
    #step4 renderEverything
    surface.fill((255,255,255))
    bullets.render()
    spaceship.render()
    pygame.display.update()

def terminate():
  pygame.quit()
  sys.exit()

class Spaceship():
  def __init__(self):
    self.height = 32
    self.width = 28

    self.ssIMG = pygame.image.load("Ships/Ship_1.png")

    self.centerx = screenSize[0] / 2
    self.centery = screenSize[1] / 2

    self.speed = 5
    self.color = allColors[9]

    self.moveLeft, self.moveRight, self.moveUp, self.moveDown = False, False, False, False

    self.rect = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)


  def update(self):
    if self.moveLeft and self.rect.left > 0:
      self.rect.centerx -= self.speed
    if self.moveRight and self.rect.right < screenSize[0] - 1:
      self.rect.centerx += self.speed
    if self.moveUp and self.rect.top > 0:
      self.rect.centery -= self.speed
    if self.moveDown and self.rect.bottom < screenSize[1] - 1:
      self.rect.centery += self.speed

  def render(self):
    surface.blit(self.ssIMG, self.rect)

class Bullet():
  def __init__(self, spaceship):
    self.bulletIMG = pygame.image.load("Ships/Ship_1.png")

    self.width = 8
    self.height = 12

    self.centerx = spaceship.rect.centerx
    self.centery = spaceship.rect.centery

    self.color = allColors[4]

    self.speed = 16

    self.isShooting = False

    self.listOfBullets = []

  def update(self, spaceship):
    for i in range(len(self.listOfBullets)):
      if i >= len(self.listOfBullets):
        break
      if self.listOfBullets[i]['counter'] >= 64:
        del self.listOfBullets[i]
        continue
      self.listOfBullets[i]['rect'].centery -= self.speed
      self.listOfBullets[i]['counter'] += 1

    if self.isShooting:
      self.listOfBullets.append({
      'rect':pygame.Rect(spaceship.rect.centerx - self.width / 2, spaceship.rect.centery - self.height, self.width, self.height),
      'counter':0
      })

  def render(self):
    for i in range(len(self.listOfBullets)):
      surface.blit(self.bulletIMG, self.listOfBullets[i]['rect'])

main()