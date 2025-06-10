import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown = self.shot_cooldown - dt
        if self.shot_cooldown < 0:
            self.shot_cooldown = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        else:
            shot = Shot(self.position.x, self.position.y)
            shot_direction = pygame.Vector2(0, 1)
            shot_direction = shot_direction.rotate(self.rotation)
            shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
            shot.velocity = shot_velocity
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
        
    def draw(self, surface):
        white = (255, 255, 255)
        pygame.draw.circle(surface, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position
