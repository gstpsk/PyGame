import pygame
import os

# Define globals
WIDTH, HEIGHT = 900, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption("Bongo sauce")

# Define colours
BG = (1, 9, 22)
WHITE = (255, 255, 255)

# Sprite dimensions
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 64, 64

# Define sprites
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'Nebula.png'))
SPACESHIPS_IMAGE = pygame.image.load(os.path.join('Assets', 'BlueRedGreen_Spacecraft_V1.0.png'))

size = width, height = (32, 32)

BLUE_SPACESHIP_IMAGE = pygame.Surface(size, pygame.SRCALPHA)
BLUE_SPACESHIP_IMAGE.blit(SPACESHIPS_IMAGE, (0, 0), (32, 0, 32, 32))
RED_SPACESHIP_IMAGE = pygame.Surface(size, pygame.SRCALPHA)
RED_SPACESHIP_IMAGE.blit(SPACESHIPS_IMAGE, (0, 0), (32, 64, 32, 32))

BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
BLUE_SPACESHIP = pygame.transform.scale(BLUE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

def draw_window(player):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(BLUE_SPACESHIP, (player.x, player.y))
    pygame.display.update()


# Main game loop function
def main():
    # Place player on centre of screen
    player = pygame.Rect(WIDTH/2-SPACESHIP_WIDTH, HEIGHT/2-SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:  # Main game loop
        clock.tick(FPS)
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(player)
    print("Thanks for playing!")
    pygame.quit()


# Only run if executed directly
if __name__ == "__main__":
    main()
