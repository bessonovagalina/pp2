import pygame
import random
import sys
import time
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600

CELL = 30

font = pygame.font.Font(None, 36)
game_over = font.render("GAME OVER", True, colorBLACK)

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    # def move(self):
    #     head = self.body[0]
    #     self.body.pop()

    #     new_x = head.x + self.dx
    #     new_y = head.y + self.dy

    #     new_head = Point(new_x, new_y)
    #     self.body.insert(0, new_head)

    def move(self):
        head = self.body[0]
        new_x = head.x + self.dx
        new_y = head.y + self.dy

        # Проверка на столкновение с телом
        for segment in self.body[1:]:
            if new_x == segment.x and new_y == segment.y:
                # Если голова столкнулась с телом, завершаем игру
                time.sleep(0.5)
                screen.fill(colorRED)
                screen.blit(game_over, (130,250))
                pygame.display.flip()
                time.sleep(1)
                pygame.quit()
                sys.exit()

        # Ограничение движения змейки по экрану
        if new_x < 0:
            new_x = WIDTH // CELL - 1
        elif new_x >= WIDTH // CELL:
            new_x = 0
        if new_y < 0:
            new_y = HEIGHT // CELL - 1
        elif new_y >= HEIGHT // CELL:
            new_y = 0

        # Если голова достигает границы экрана, меняем направление движения
        if new_y == 0:  # Верхняя граница
            new_y = 0
            self.dx = 1
            self.dy = 0
        elif new_y >= HEIGHT // CELL - 1:  # Нижняя граница
            new_y = HEIGHT // CELL - 1
            self.dx = 1
            self.dy = 0
        elif new_x == 0:  # Левая граница
            new_x = 0
            self.dx = 0
            self.dy = 1
        elif new_x >= WIDTH // CELL - 1:  # Правая граница
            new_x = WIDTH // CELL - 1
            self.dx = 0
            self.dy = -1

        # Обновляем положение головы и остальных сегментов тела
        self.body.pop()
        new_head = Point(new_x, new_y)
        self.body.insert(0, new_head)


    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            if head in self.body[1:]:
                # Если голова столкнулась с телом, завершаем игру
                time.sleep(0.5)
                screen.fill(colorRED)
                screen.blit(game_over, (130,250))
                pygame.quit()
                sys.exit()
            self.body.append(Point(head.x, head.y))
            food.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT :
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN :
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP :
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()

    pygame.display.flip()
    clock.tick(FPS)