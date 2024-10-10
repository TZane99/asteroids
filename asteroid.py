import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vec1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        vec2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        aster1 = Asteroid(self.position.x,self.position.y, new_rad)
        aster2 = Asteroid(self.position.x,self.position.y, new_rad)
        aster1.velocity = vec1 * 1.2
        aster2.velocity = vec2 * 1.2