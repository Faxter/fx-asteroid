from configparser import ConfigParser

import pygame

from CircleShape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        self.__constants = ConfigParser()
        self.__constants.read("constants.ini")
        super().__init__(x, y, self.__constants.getint("PLAYER", "RADIUS"))
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), self.__constants.getint("PLAYER", "LINE_WIDTH"))
