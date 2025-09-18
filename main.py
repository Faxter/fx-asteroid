from configparser import ConfigParser

import pygame


def main():
    constants = ConfigParser()
    constants.read("constants.ini")

    width = int(constants.get("SCREEN", "WIDTH"))
    height = int(constants.get("SCREEN", "HEIGHT"))

    print("Starting Asteroids!")
    print(f"Screen width: {width}")
    print(f"Screen height: {height}")

    pygame.init()
    screen = pygame.display.set_mode((width, height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
