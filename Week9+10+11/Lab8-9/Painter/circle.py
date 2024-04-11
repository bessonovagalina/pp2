import math
import pygame

pygame.init()

def calculate_circle_radius(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def circle_draw(done):
    LMBpressed = False
    THICKNESS = 5
    colorRED = (255, 0, 0)
    
    currX = 0
    currY = 0
    
    prevX = 0
    prevY = 0
    
    done = False
    while not done:
    
        for event in pygame.event.get():
            if LMBpressed:
                screen.blit(base_layer, (0, 0))
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # print("LMB pressed!")
                LMBpressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]
    
            if event.type == pygame.MOUSEMOTION:
                # print("Position of the mouse:", event.pos)
                if LMBpressed:
                    currX = event.pos[0]
                    currY = event.pos[1]
                    radius = int(calculate_circle_radius(prevX, prevY, currX, currY))
                    pygame.draw.circle(screen, colorRED, (prevX, prevY), radius, THICKNESS)
    
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # print("LMB released!")
                LMBpressed = False
                currX = event.pos[0]
                currY = event.pos[1]
                radius = int(calculate_circle_radius(prevX, prevY, currX, currY))
                pygame.draw.circle(screen, colorRED, (prevX, prevY), radius, THICKNESS)
                base_layer.blit(screen, (0, 0))
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS:
                    # print("increased thickness")
                    THICKNESS += 1
                if event.key == pygame.K_MINUS:
                    # print("reduced thickness")
                    THICKNESS -= 1
    
        pygame.display.flip()
        clock.tick(60)

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Circle Drawer")
clock = pygame.time.Clock()
base_layer = screen.copy()

circle_draw(False)
pygame.quit()