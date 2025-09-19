from configparser import ConfigParser

import pygame

from Asteroid import Asteroid
from AsteroidField import AsteroidField
from Player import Player
from Shot import Shot


def main():
    constants = ConfigParser()
    constants.read("constants.ini")

    width = constants.getint("SCREEN", "WIDTH")
    height = constants.getint("SCREEN", "HEIGHT")

    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    delta_time = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(width // 2, height // 2)

    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)

    AsteroidField.containers = updatables
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatables.update(delta_time)
        for a in asteroids:
            if a.collides(player):
                print("Game over!")
                return
        for d in drawables:
            d.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(constants.getint("PERFORMANCE", "FPS")) / 1000


if __name__ == "__main__":
    main()
