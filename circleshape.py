import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, containers=None):
        if containers is not None:
            super().__init__(containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen, color, points):
        # Base class implementation - draw a circle
        pygame.draw.circle(screen, color, self.position, self.radius)

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        if isinstance(other, CircleShape):
            return self.position.distance_to(other.position) < self.radius + other.radius
        return False

        
    