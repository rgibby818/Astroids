import pygame
import constants


def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,
                                      constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
