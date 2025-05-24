# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting Asteroids!")
  pygame.init()
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Asteroids")

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS, containers=(updatable, drawable))

  Shot.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable)
  AsteroidField.containers = (updatable,)
  asteroid_field = AsteroidField()

  clock = pygame.time.Clock()

  while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

    screen.fill((0, 0, 0))  # Fill the screen with black
    # Check for player shooting and add shots to the shots group
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      shot = player.shoot(dt)
      shots.add(shot)
      
    for sprite in updatable:
      sprite.update(dt)

    for sprite in drawable:
      if hasattr(sprite, 'triangle'):
        sprite.draw(screen, (255, 255, 255), sprite.triangle())
      else:
        sprite.draw(screen, (255, 255, 255), None)


    pygame.display.flip()  # Update the display
    
    # Check for asteroid collisions
    for asteroid in asteroid_field:
      if player.collides_with(asteroid):
        print("Game over!")
        pygame.quit()
        return

    # Check for shot collisions with asteroids
    for shot in shots:
      for asteroid in asteroid_field:
        if shot.collides_with(asteroid):
          # Remove shot and asteroid when they collide
          shots.remove(shot)
          asteroid.kill()
          break

    # Remove shots that go off-screen
    for shot in shots:
      if shot.position.x < 0 or shot.position.x > SCREEN_WIDTH or \
         shot.position.y < 0 or shot.position.y > SCREEN_HEIGHT:
        shots.remove(shot)

    clock.tick(60)
    
if __name__ == "__main__":
    main()