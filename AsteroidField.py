import random
from configparser import ConfigParser

import pygame

from Asteroid import Asteroid


class AsteroidField(pygame.sprite.Sprite):
    constants = ConfigParser()
    constants.read("constants.ini")
    SCREEN_HEIGHT = constants.getint("SCREEN", "HEIGHT")
    SCREEN_WIDTH = constants.getint("SCREEN", "WIDTH")
    MAX_RADIUS = constants.getint("ASTEROID", "MAX_RADIUS")

    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-AsteroidField.MAX_RADIUS, y * AsteroidField.SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(AsteroidField.SCREEN_WIDTH + AsteroidField.MAX_RADIUS, y * AsteroidField.SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * AsteroidField.SCREEN_WIDTH, -AsteroidField.MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(x * AsteroidField.SCREEN_WIDTH, AsteroidField.SCREEN_HEIGHT + AsteroidField.MAX_RADIUS),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, delta_time):
        self.spawn_timer += delta_time
        if self.spawn_timer > AsteroidField.constants.getfloat("ASTEROID", "SPAWN_RATE_SECONDS"):
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, AsteroidField.constants.getint("ASTEROID", "KINDS"))
            self.spawn(AsteroidField.constants.getint("ASTEROID", "MIN_RADIUS") * kind, position, velocity)
