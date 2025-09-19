from configparser import ConfigParser

import pygame

from CircleShape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.__constants = ConfigParser()
        self.__constants.read("constants.ini")
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.__constants.getint("ASTEROID", "LINE_WIDTH"))

    def update(self, delta_time):
        self.position += delta_time * self.velocity
