from circleshape import *
from constants import *
import random

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
        
    def split(self):
        from asteroidfield import AsteroidField
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            AsteroidField.instance.spawn(radius, self.position, new_vector1 * 1.2)
            AsteroidField.instance.spawn(radius, self.position, new_vector2 * 1.2)