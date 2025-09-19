from configparser import ConfigParser

import pygame

from Player import Player


def main():
    constants = ConfigParser()
    constants.read("constants.ini")

    width = constants.getint("SCREEN", "WIDTH")
    height = constants.getint("SCREEN", "HEIGHT")

    print("Starting Asteroids!")
    print(f"Screen width: {width}")
    print(f"Screen height: {height}")

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    delta_time = 0
    player = Player(width // 2, height // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(constants.getint("PERFORMANCE", "FPS"))


if __name__ == "__main__":
    main()
