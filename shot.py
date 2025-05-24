import pygame
from circleshape import CircleShape
from pygame import Vector2, draw
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, containers=None):
        super().__init__(x, y, SHOT_RADIUS, containers=containers)
        self.velocity = Vector2(0, 100)
        
    def update(self, dt):
        # Update the shot's position based on its velocity
        self.position += self.velocity * dt

    def draw(self, screen, color, points):
        # Draw a small circle for the shot
        pygame.draw.circle(screen, color, self.position, self.radius)