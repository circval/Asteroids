from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.Surface((self.radius * 3, self.radius * 3))
        self.rect = self.image.get_rect()
           

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2) + forward * self.radius
        b = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2) - forward * self.radius - right
        c = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2) - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        self.rect.center = self.position
        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, "white", self.triangle(), 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            rev_dt = dt * -1
            self.rotate(rev_dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt