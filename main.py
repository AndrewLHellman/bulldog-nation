import pygame
from Game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode([1920, 1080])
    running = True
    game = Game(screen)

    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()
        game.update(keys, screen)
        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        game.detectPlayerCollision()
        game.render(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()