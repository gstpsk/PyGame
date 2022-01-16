import pygame
import os

# Define globals
WIDTH, HEIGHT = 900, 900
FPS = 60
VELOCITY = 5
CAPTION = "Bongo sauce"

# Define colours
BG = (1, 9, 22)
WHITE = (255, 255, 255)

# Sprite dimensions
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 64, 64

# Load images
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'Nebula.png'))
SPACESHIPS_IMAGE = pygame.image.load(os.path.join('Assets', 'BlueRedGreen_Spacecraft_V1.0.png'))
FRIENDLY_PARTICLE_IMAGE = pygame.image.load(os.path.join('Assets', 'PNG_Animations', 'Shots', 'Shot4', 'shot4_exp3.png'))

# Create surfaces
size = width, height = (32, 32)
BLUE_SPACESHIP_IMAGE = pygame.Surface(size, pygame.SRCALPHA)
RED_SPACESHIP_IMAGE = pygame.Surface(size, pygame.SRCALPHA)
#FRIENDLY_PARTICLE_SURF = pygame.Surface((64, 64))

# Write sprites to surfaces
BLUE_SPACESHIP_IMAGE.blit(SPACESHIPS_IMAGE, (0, 0), (32, 0, 32, 32))
RED_SPACESHIP_IMAGE.blit(SPACESHIPS_IMAGE, (0, 0), (32, 64, 32, 32))
#FRIENDLY_PARTICLE_IMAGE.blit(FRIENDLY_PARTICLE_IMAGE, (0, 0), (32, 0, 32, 32))

# Resize sprites if needed
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
BLUE_SPACESHIP = pygame.transform.scale(BLUE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
FRIENDLY_PARTICLE = pygame.transform.scale(FRIENDLY_PARTICLE_IMAGE, (32, 32))