import pygame
import math

pygame.init()

# Set up the simulation window
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Physics Playground")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define a particle class
class Particle:
    def __init__(self, x, y, radius=10):
        self.x = x
        self.y = y
        self.radius = radius
        self.prev_x = x
        self.prev_y = y

    def update_position(self, dt):
        # Verlet integration to update position
        temp_x = self.x
        temp_y = self.y
        self.x = 2 * self.x - self.prev_x
        self.y = 2 * self.y - self.prev_y + 9.81 * dt**2
        self.prev_x = temp_x
        self.prev_y = temp_y

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)


particles = []
rectcoordnate = [100, 10]

running = True
clock = pygame.time.Clock()

while running:
    dt = clock.tick(60) / 1000.0  # Time in seconds since last update
    pygame.draw.rect(screen, BLACK, (rectcoordnate[0], rectcoordnate[1], 70, 65))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            particles.append(Particle(x, y))

        key_input = pygame.key.get_pressed()   
        if key_input[pygame.K_LEFT]:
            rectcoordnate[0] -= 10
        if key_input[pygame.K_RIGHT]:
            rectcoordnate[0] += 10

    # Update particle positions
    for particle in particles:
        particle.update_position(dt)

    # Clear the screen
    screen.fill(WHITE)

    # Draw particles
    for particle in particles:
        particle.draw()

    # Update the display
    pygame.display.flip()

pygame.quit()