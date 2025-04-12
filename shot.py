from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    containers = []
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        for container in Shot.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)