# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  print("Starting Asteroids!")
  pygame.init()
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Asteroids")

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)

  Asteroid.containers = (updatable, drawable)
  asteroid = Asteroid(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, ASTEROID_MIN_RADIUS)

  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  clock = pygame.time.Clock()

  while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

    screen.fill((0, 0, 0))  # Fill the screen with black
    for sprite in updatable:
      sprite.update(dt)

    for sprite in drawable:
      sprite.draw(screen, (255, 255, 255), sprite.triangle())


    pygame.display.flip()  # Update the display
    clock.tick(60)

    

if __name__ == "__main__":
    main()