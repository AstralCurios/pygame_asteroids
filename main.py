# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

BLACK = (0, 0, 0)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    game_clock = pygame.time.Clock() # Create a clock object to manage the frame rate
    dt = 0 #Initialize delta time

    # Create sprite groups for managing game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Assign the sprite groups to the Player class and create player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 


    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Main game loop
    while True:
        for event in pygame.event.get(): #Let player quit the game
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) # Update all updatable objects

        screen.fill(BLACK)  # Fill the screen with black

        for obj in drawable:   # Draw all drawable objects
            obj.draw(screen)

        pygame.display.flip() #Update the full display Surface to the screen
        game_clock.tick(60)  # Cap the frame rate at 60 FPS
        dt = game_clock.get_time() / 1000.0  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
