from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        
    def draw(self, surface):
        white = (255, 255, 255)
        pygame.draw.circle(surface, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            rotated_vector_1 = self.velocity.rotate(angle)
            rotated_vector_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = rotated_vector_1 * 1.2
            new_asteroid_2.velocity = rotated_vector_2 * 1.2