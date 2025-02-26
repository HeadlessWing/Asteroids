import pygame
from constants import *
from circleshape import *
from player import *

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updateable, drawable)

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
        updateable.update(dt)
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        #limits framerate to 60 fps
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()