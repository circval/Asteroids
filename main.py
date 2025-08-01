from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *
import pygame
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField()
    
    loop = 1
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while loop == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for a in asteroids:
            if a.collision(player) == True:
                    print("Game Over!")
                    sys.exit()

        for a in asteroids:
            for s in shots:
                if s.collision(a):
                    s.kill()
                    a.split()

if __name__ == "__main__":
    main()