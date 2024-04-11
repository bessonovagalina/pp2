import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
white = (255, 255, 255)

done = False
is_red = True
#начальные координаты 
x = 30
y = 30

radius = 25 

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < 770: #чтоб не выходил за пределы 
        x += 20
    if keys[pygame.K_LEFT] and x > 30: 
        x -= 20
    if keys[pygame.K_DOWN] and y < 570:
        y += 20
    if keys[pygame.K_UP] and y > 30:
        y -= 20
        
    screen.fill(white)

    pygame.draw.circle(screen, red, (x, y), radius)  # нарисовать круг красного цвета
    
    pygame.display.flip()
    clock.tick(60)
