import sys
import pygame
from pygame.locals import *
import time

class MickeyClock:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700, 700))
        self.clock = pygame.time.Clock()

        self.image_mickey_right = pygame.image.load("./Week9+10+11\Lab7\mickey_right.png").convert_alpha()
        self.image_mickey_left = pygame.image.load("./Week9+10+11\Lab7\mickey_left.png").convert_alpha()
        self.BACKGROUND = pygame.image.load("./Week9+10+11\Lab7\BACKGROUND.png").convert_alpha()

        # Изменяем размер фонового изображения
        self.BACKGROUND = pygame.transform.scale(self.BACKGROUND, (700, 700))
        #self.image_mickey_right = pygame.transform.scale(self.image_mickey_right, (60, 100))
        #self.image_mickey_left = pygame.transform.scale(self.image_mickey_left, (60, 100))

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.draw_clock()
            pygame.display.flip()
            self.clock.tick(60)

    def draw_clock(self):
        self.window.blit(self.BACKGROUND, (0, 0))

        current_time = time.localtime()
        minute_angle = (current_time.tm_min / 60) * 360
        second_angle = (current_time.tm_sec / 60) * 360

        self.draw_hand(self.image_mickey_right, minute_angle)
        self.draw_hand(self.image_mickey_left, second_angle)

    def draw_hand(self, image, angle):
        rotated_image = pygame.transform.rotate(image, -angle)
        rect = rotated_image.get_rect(center=(350, 350))
        self.window.blit(rotated_image, rect)

if __name__ == "__main__":
    clock = MickeyClock()
