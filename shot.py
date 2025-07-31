from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((self.radius * 3, self.radius * 3))
        self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        pygame.draw.circle(self.image, "white", (self.image.get_width() / 2, self.image.get_height() / 2), SHOT_RADIUS, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = (int(self.position.x), int(self.position.y))