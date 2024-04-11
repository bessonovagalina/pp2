import pygame
from rectangle import *

pygame.init()


def move_rectangle(rect, dx, dy):
    rect.x += dx
    rect.y += dy


def main():
    running = True
    rectangle = pygame.Rect(100, 100, 200, 150)
    while running:
        screen.fill(COLOR_WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_rectangle(rectangle, 0, -5)
                elif event.key == pygame.K_DOWN:
                    move_rectangle(rectangle, 0, 5)
                elif event.key == pygame.K_LEFT:
                    move_rectangle(rectangle, -5, 0)
                elif event.key == pygame.K_RIGHT:
                    move_rectangle(rectangle, 5, 0)

        screen.blit(base_layer, (0, 0))
        pygame.draw.rect(screen, COLOR_RED, rectangle, THICKNESS)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()