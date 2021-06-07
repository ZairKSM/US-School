import pygame
import os
import random
import math
import winsound
# winsound.PlaySound("explosion.wav", winsound.SND_ALIAS)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)
wn = pygame.display.set_mode((1920, 1020))
clock = pygame.time.Clock()


vel = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        z = random.randint(0, 101)
        if z <= 51:
            self.original_image = pygame.Surface((75,75))
        else:
            self.original_image = pygame.Surface((75,75))
        if z == 41:
            self.original_image = pygame.Surface((75,75))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = pygame.math.Vector2((0, -1))
        self.velocity = 5
        self.position = pygame.math.Vector2(x, y)
        self.x = pygame.math.Vector2(x)
        self.y = pygame.math.Vector2(y)
        self.health = 10
        self.visible = True


    def point_at(self, x, y):
        self.direction = pygame.math.Vector2(x, y) - self.rect.center
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        angle = self.direction.angle_to((0, -1))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, x, y):
        self.position -= self.direction * y * self.velocity
        self.position += pygame.math.Vector2(-self.direction.y, self.direction.x) * x * self.velocity
        self.rect.center = round(self.position.x), round(self.position.y)


    def reflect(self, NV):
        self.direction = self.direction.reflect(pygame.math.Vector2(NV))

    def update(self):
        self.position += self.direction * self.velocity
        self.rect.center = round(self.position.x), round(self.position.y)

    def hit(self, player):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        distance = math.sqrt(math.pow(player.x - player.x(), 2) + math.pow(player.y - player.y(), 2))
        if distance < 20:
            return True

        else:
            return False



    def move(self, x, y, clamp_rect):
        self.position -= self.direction * y * self.velocity
        self.position += pygame.math.Vector2(-self.direction.y, self.direction.x) * x * self.velocity
        self.rect.center = round(self.position.x), round(self.position.y)

        if self.rect.left < clamp_rect.left:
            self.rect.left = clamp_rect.left
            self.position.x = self.rect.centerx
        if self.rect.right > clamp_rect.right:
            self.rect.right = clamp_rect.right
            self.position.x = self.rect.centerx
        if self.rect.top < clamp_rect.top:
            self.rect.top = clamp_rect.top
            self.position.y = self.rect.centery
        if self.rect.bottom > clamp_rect.bottom:
            self.rect.bottom = clamp_rect.bottom
            self.position.y = self.rect.centery

    class Projectile(object):
        def __init__(self, x, y, radius, color, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)






player = Player(200, 200)
all_sprites = pygame.sprite.Group(player)


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            player.point_at(*event.pos)

    pygame.draw.rect(wn, (0, 0, 0), (50, 50, 10000, 100000))



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move(0, -1, wn.get_rect())


    wn.fill((255, 255, 255))
    all_sprites.draw(wn)
    pygame.display.update()