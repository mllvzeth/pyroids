# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
  print("Starting Asteroids!")
  pygame.init()
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Asteroids")

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()