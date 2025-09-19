import random
from configparser import ConfigParser

import pygame

from src.CircleShape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.__constants = ConfigParser()
        self.__constants.read("res/constants.ini")
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.__constants.getint("ASTEROID", "LINE_WIDTH"))

    def update(self, delta_time):
        self.position += delta_time * self.velocity

    def split(self):
        self.kill()
        asteroid_min_radius = self.__constants.getint("ASTEROID", "MIN_RADIUS")
        if self.radius <= asteroid_min_radius:
            return
        split_off_angle = random.uniform(20, 50)
        new_direction_1 = self.velocity.rotate(split_off_angle)
        new_direction_2 = self.velocity.rotate(-split_off_angle)
        new_radius = self.radius - asteroid_min_radius
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = 1.2 * new_direction_1
        a2.velocity = 1.2 * new_direction_2
