from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        
    def draw(self, surface):
        white = (255, 255, 255)
        pygame.draw.circle(surface, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position