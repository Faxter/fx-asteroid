from configparser import ConfigParser

import pygame


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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        delta_time = clock.tick(constants.getint("PERFORMANCE", "FPS"))


if __name__ == "__main__":
    main()
