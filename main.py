from sys import exit
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Delta variable for use to calculate the time since last frame was updated
    dt = 0

    # Game Loop
    while True:
        # Exit program if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
            if type(obj) == Player:
                obj.shot_timer -= dt
        
        for obj in asteroids:
            if obj.collision(player):
                print("Game Over!")
                exit()

            for shot in shots:
                if obj.collision(shot):
                    obj.split()
                    shot.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Update the full display surface to the screen
        pygame.display.flip()
        # update clock to keep framerate at 60FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
