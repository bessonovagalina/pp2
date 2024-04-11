import pygame
from rectangle import rectangle_draw

# Инициализация Pygame
pygame.init()

# Создание дисплея
screen = pygame.display.set_mode((640, 480))

# Флаг для отслеживания необходимости рисования прямоугольника
draw_rectangle = False

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                draw_rectangle = True  # Установка флага при нажатии левой стрелки

    if draw_rectangle:
        rectangle_draw(screen)  # Предполагается, что rectangle_draw принимает аргумент screen
        draw_rectangle = False  # Сброс флага после выполнения функции

    # Обновление дисплея
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()