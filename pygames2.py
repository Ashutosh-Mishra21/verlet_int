import pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Ball Bouncing")
screen = pygame.display.set_mode((1000, 800))

clock = pygame.time.Clock()

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

ball1 = pygame.draw.circle(
    surface = screen, color = red, center = [10,40] , radius = 20 
)

ball2 = pygame.draw.circle(
    surface = screen, color = red, center = [400,500] , radius = 20 
)

speed1 = [1,1]
speed2 = [3,3]

while True:

    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    ball1 = ball1.move(speed1)

    if ball1.left <= 0 or ball1.right >= 1000:
        speed1[0] = -speed1[0]
    if ball1.top <= 0 or ball1.bottom >= 800:
        speed1[1] = -speed1[1]

    pygame.draw.circle(surface = screen, color = red, center = ball1.center, radius = 20)

    ball2 = ball2.move(speed2)

    if ball2.left <= 0 or ball2.right >= 1000:
        speed2[0] = -speed2[0]
    if ball2.top <= 0 or ball2.bottom >= 800:
        speed2[1] = -speed2[1]

    pygame.draw.circle(surface = screen, color = red, center = ball2.center, radius = 20)

    pygame.display.flip()