from configparser import ConfigParser

import pygame

from src.CircleShape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        self.__constants = ConfigParser()
        self.__constants.read("res/constants.ini")
        super().__init__(x, y, self.__constants.getint("SHOT", "RADIUS"))

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.__constants.getint("SHOT", "LINE_WIDTH"))

    def update(self, delta_time):
        self.position += delta_time * self.velocity
