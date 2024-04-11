import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)

clock = pygame.time.Clock()

LMB_pressed = False
THICKNESS = 5

curr_pos = (0, 0)
prev_pos = (0, 0)


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


def draw_rect(start_pos, end_pos):
    pygame.draw.rect(screen, COLOR_RED, calculate_rect(*start_pos, *end_pos), THICKNESS)


def main():
    global LMB_pressed, prev_pos

    running = True

    while running:
        screen.fill(COLOR_WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMB_pressed = True
                prev_pos = event.pos
            elif event.type == pygame.MOUSEMOTION and LMB_pressed:
                print("Position of the mouse:", event.pos)
                curr_pos = event.pos
                draw_rect(prev_pos, curr_pos)
                prev_pos = curr_pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMB_pressed = False
                curr_pos = event.pos
                draw_rect(prev_pos, curr_pos)
                prev_pos = curr_pos
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS:
                    print("increased thickness")
                    THICKNESS += 1
                elif event.key == pygame.K_MINUS:
                    print("reduced thickness")
                    THICKNESS -= 1

        screen.blit(base_layer, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()