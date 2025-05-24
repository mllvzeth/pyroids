from constants import *
from circleshape import CircleShape
from pygame import Vector2, draw, key, K_a, K_d, K_w, K_s, K_SPACE
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius, rotation = 0, containers=None):
        super().__init__(x, y, radius, containers=containers)
        self.rotation = rotation

    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen, color, points):
        points = self.triangle()
        draw.polygon(screen, color, points, 2)

    def update(self, dt):
        keys = key.get_pressed()

        if keys[K_a]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[K_d]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[K_w]:
            self.move(dt)
        if keys[K_s]:
            self.move(-dt)
        if keys[K_SPACE]:
            shot = self.shoot(dt)
    
    def move(self, dt):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        forward = Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, containers=Shot.containers)
        shot.velocity = forward * PLAYER_SHOT_SPEED
        return shot