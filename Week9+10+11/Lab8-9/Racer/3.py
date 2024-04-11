import pygame
import random
import sys
import time

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

BACKGROUND = pygame.image.load("./Week9+10+11\Lab8-9\Racer\AnimatedStreet.png")

clock = pygame.time.Clock()

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Week9+10+11\Lab8-9\Racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Week9+10+11\Lab8-9\Racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)
# random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("Week9+10+11\Lab8-9\Racer\coin.png")
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)))
    def move(self):
        new_position = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
        self.rect.center = new_position

SPEED = 5

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
E1 = Enemy()
coin = Coin()

enemies.add(E1)
all_sprites.add(P1, E1, coin)
coins = pygame.sprite.Group(coin)

done = False

FPS = 60

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(colorRED)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()
        
    pygame.display.flip()
    clock.tick(FPS)