# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = updatable, drawable
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            for b in asteroids:
                if a != b and a.check_collision(b):
                    a.velocity, b.velocity = b.velocity, a.velocity
        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                running = False
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
