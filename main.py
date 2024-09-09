import pygame
import constants
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()

    # Set screen resolution
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,
                                      constants.SCREEN_HEIGHT))
    # Clock object used to track an amount of time and is able to control framerate
    clock = pygame.time.Clock()
    # Delta variable for use to calculate the time since last frame was updated
    dt = 0

    # Position player on program launch in center of the rendered screen
    player = Player(constants.SCREEN_WIDTH / 2,
                           constants.SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        # Exit program if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the screen with black background
        screen.fill(000)
        # Update player location
        player.update(dt)
        # Draw Player on screen
        player.draw(screen)
        # Update the full display surface to the screen
        pygame.display.flip()
        # update clock to keep framerate at 60FPS
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
