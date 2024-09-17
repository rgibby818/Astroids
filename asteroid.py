import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           "white",
                           self.position,
                           self.radius,
                           2)
    
    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vectors = (self.velocity.rotate(angle), self.velocity.rotate(-angle))
        radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position[0], self.position[1], radius)
        new_asteroid_2 = Asteroid(self.position[0], self.position[1], radius)
        new_asteroid_1.velocity = vectors[0] * 1.2
        new_asteroid_2.velocity = vectors[1] * 1.2

