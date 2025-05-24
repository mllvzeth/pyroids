from circleshape import CircleShape
from pygame import Vector2, draw

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, containers=None):
        super().__init__(x, y, radius, containers=containers)
        self.rotation = 0  # Add rotation for the asteroid
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += 10 * dt  # Add some rotation to the asteroid
        
    def triangle(self):
        # Return a list of points that form a polygon for the asteroid
        points = []
        # Create a polygon with 6-10 sides (randomized for each asteroid)
        sides = 8  # You can make this random if you want more variety
        for i in range(sides):
            angle = (i / sides) * 360 + self.rotation
            # Add some randomness to the radius to make it look more like an asteroid
            r = self.radius * (0.8 + 0.4 * (hash(str(self.position) + str(i)) % 100) / 100)
            offset = Vector2(0, -r).rotate(angle)
            points.append(self.position + offset)
        return points
        
    def draw(self, screen, color, points, line_width=1):
        """Draw the asteroid as a polygon"""
        draw.polygon(screen, color, points, line_width)