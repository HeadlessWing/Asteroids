import pygame
from constants import *
from circleshape import *
from player import *


def main():
    pygame.init
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 #delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        #limits framerate to 60 fps
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()