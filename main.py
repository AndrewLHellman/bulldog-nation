import pygame
from Game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode([1920, 1080])
    running = True
    game = Game(screen)
    clock = pygame.time.Clock()
    background_img = pygame.image.load('./source/sprites/Background.jpg').convert()
    background_img = pygame.transform.scale(background_img, (screen.get_width(), screen.get_height()))
    background_rect = background_img.get_rect()

    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(background_img, background_rect)
        keys = pygame.key.get_pressed()
        game.update(keys, screen)
        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        game.render(screen)

        pygame.display.flip()

    clock.tick(1000/60)

    pygame.quit()

if __name__ == "__main__":
    main()