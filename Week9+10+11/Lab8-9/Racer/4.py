import pygame
import random
import sys
import time
#from pygame.locals import *

pygame.init()
#pygame.mixer.init()
count = 0
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)  # None используется для использования шрифта по умолчанию, размер 36
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

game_over = font.render("GAME OVER", True, colorBLACK)

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

class Coin(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("./Week9+10+11\Lab8-9\Racer\coin.png")
        self.image = pygame.transform.scale(original_image, (50, 50))  # новые размеры
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

# random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2

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

SPEED = 5

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
coins=pygame.sprite.Group()

P1 = Player()
E1 = Enemy()
C1 = Coin()  # Создание монеты

enemies.add(E1)
coins.add(C1)  # Добавление монеты в группу монет
all_sprites.add(P1, E1, C1)  # Добавление монеты в группу всех спрайтов
done = False

# Перемещение монетки, если она пересекается с вражеской машинкой

for coin in coins:
    if pygame.sprite.spritecollideany(coin, enemies):
       coin.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))# не работает нормально 

FPS = 60

while not done:
    #pygame.mixer.Sound("./Week9+10+11\Lab8\Racer\subway-surfers-soundtrack_456240184.wav").play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    while pygame.sprite.spritecollideany(E1, coins):
        coin.move()
    if pygame.sprite.spritecollideany(P1, coins):
       count+=1
       coin.move() #кажется неправильно 
    if pygame.sprite.spritecollideany(P1, enemies):

        pygame.mixer.Sound("./Week9+10+11\Lab8\Racer\crash.wav").play()
        time.sleep(0.5)
        
        screen.fill(colorRED)
        screen.blit(game_over, (130,250))
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()

    text = font.render(f"Coins: {count}", True, colorBLACK)
    screen.blit(text, (10, 10))  # Отображение текста в левом верхнем углу

    pygame.display.flip()
    clock.tick(FPS)