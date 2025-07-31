from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius, 2)
        self.position += (self.velocity * dt)
        self.rect.center = self.position