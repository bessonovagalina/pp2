import pygame
import random
import sys
import time

pygame.init()
#pygame.mixer.init()
count = 0
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)
colorRED = (255, 0, 0)
colorBLACK = (0, 0, 0)

BACKGROUND = pygame.image.load("Week9+10+11\Lab8-9\Racer\AnimatedStreet.png")
#coin_sound = pygame.mixer.Sound("coin.wav")
#rash_sound = pygame.mixer.Sound("crash.wav")
#pygame.mixer.music.load("background.wav")
#pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().init()
        self.image = pygame.image.load("Week9+10+11\Lab8-9\Racer\Player.png")
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 55))
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().init()
        original_image = pygame.image.load("Week9+10+11\Lab8-9\Racer\coin.png")
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)))
    def move(self):
        new_position = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
        self.rect.center = new_position

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Week9+10+11\Lab8-9\Racer\Enemy.png")
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH-50), 35))

SPEED = 2
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)
done = False

#pygame.mixer.music.load("background.wav")
#pygame.mixer.music.play(-1)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1

    player.move()
    enemy.rect.y += SPEED if enemy.rect.y < HEIGHT else -35
    coin.rect.y += SPEED if coin.rect.y < HEIGHT else coin.move()

    if pygame.sprite.spritecollide(player, coins, dokill=True):
        count += 1
        #coin_sound.play()
        coin.move()

    screen.blit(BACKGROUND, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollide(player, enemies, dokill=False):
        #crash_sound.play()
        time.sleep(1)
        done = True

    score_text = font.render(f"Coins: {count}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()