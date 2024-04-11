import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # Заполнение фона белым цветом

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()
current_shape = None

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle_radius(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

# Основной цикл
running = True
LMBpressed = False
prevX, prevY = 0, 0
THICKNESS = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_shape = 'rectangle'
            elif event.key == pygame.K_RIGHT:
                current_shape = 'circle'
            elif event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:
                THICKNESS -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if current_shape == 'rectangle':
                pygame.draw.rect(base_layer, colorRED, calculate_rect(prevX, prevY, event.pos[0], event.pos[1]), THICKNESS)
            elif current_shape == 'circle':
                radius = int(calculate_circle_radius(prevX, prevY, event.pos[0], event.pos[1]))
                pygame.draw.circle(base_layer, colorRED, (prevX, prevY), radius, THICKNESS)
        elif event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                screen.blit(base_layer, (0, 0))
                if current_shape == 'rectangle':
                    pygame.draw.rect(screen, colorRED, calculate_rect(prevX, prevY, event.pos[0], event.pos[1]), THICKNESS)
                elif current_shape == 'circle':
                    radius = int(calculate_circle_radius(prevX, prevY, event.pos[0], event.pos[1]))
                    pygame.draw.circle(screen, colorRED, (prevX, prevY), radius, THICKNESS)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()