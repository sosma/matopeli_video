import pygame
from time import sleep
from random import randint


points = 0
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 12)

background_colour = (255,255,255)
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game')
screen.fill(background_colour)
running = True

snake_position = [(30,10), (10,10), (10,10)]
apple_position = (randint(0, 79)*10, randint(0,59)*10)
snake_direction = (10, 0)
gameover = False

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)

while running:
    if not gameover:
        screen.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and  snake_direction != (10, 0):
                    snake_direction = (-10, 0)
                if event.key == pygame.K_d and snake_direction != (-10, 0):
                    snake_direction = (10, 0)
                if event.key == pygame.K_w and snake_direction != (0,10):
                    snake_direction = (0,-10)
                if event.key == pygame.K_s and snake_direction != (0,-10):
                    snake_direction = (0,10)

        """
        piirretään käärme ja omena ja pisteet
        """    
        snake_position_new = [(snake_position[0][0] + snake_direction[0],snake_position[0][1] + snake_direction[1])]
        for position in snake_position:
            snake_position_new.append(position)
        old_position = snake_position_new.pop()
        snake_position = snake_position_new
        for position in snake_position:
            pygame.draw.rect(screen, (0,255, 0), (position[0], position[1], 10, 10))

        pygame.draw.rect(screen, (255,0, 0), (apple_position[0], apple_position[1], 10, 10))
        text_surface = font.render('Pisteet: %s' % str(points), True, (0, 0, 0))
        screen.blit(text_surface, dest=(0,0))

        
        """
        syödäänkö omena
        """
        if snake_position[0] == apple_position:
            snake_position.append(old_position)
            points+=1
            apple_position = (randint(0, 79)*10, randint(0,59)*10)
            while apple_position in snake_position:
                apple_position = (randint(0, 79)*10, randint(0,59)*10)


        """
        törmääkö mato itseensä
        """
        if snake_position[0][1] > 590 or snake_position[0][1] < 0:
            gameover = True
        if snake_position[0][0] > 790 or snake_position[0][0] < 0:
            gameover = True
        for position in snake_position[1:]:
            if snake_position[0] == position:
                gameover = True
                


        pygame.display.flip()
        screen.fill(background_colour)
    if gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    sleep(0.1)

