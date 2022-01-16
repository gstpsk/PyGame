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
PINK = (238, 29, 119)

# Load fonts
pygame.font.init()
DEATH_FONT = pygame.font.Font(os.path.join('Assets', 'fonts', 'StalinistOne-Regular.ttf'), 64)
MAIN_FONT = pygame.font.SysFont('Source Code Pro', 30)

# Sprite dimensions
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 64, 64

# Load images
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'Nebula.png'))
SPACESHIPS_IMAGE = pygame.image.load(os.path.join('Assets', 'BlueRedGreen_Spacecraft_V1.0.png'))
FRIENDLY_PARTICLE_IMAGE = pygame.image.load(os.path.join('Assets', 'PNG_Animations', 'Shots', 'Shot4', 'shot4_exp3.png'))
ENEMY1_IMAGE = pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Ship1', 'Ship1.png'))
EXPLOSION_SPRITE = [pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_1.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_2.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_3.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_4.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_5.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_6.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_7.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_8.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_9.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_10.png')),
                    pygame.image.load(os.path.join('Assets', 'PNG_Parts&Spriter_Animation', 'Explosions', 'Explosion1', 'Explosion1_11.png'))]

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
BLUE_SPACESHIP_SMOL = pygame.transform.scale(BLUE_SPACESHIP_IMAGE, (40, 40))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
FRIENDLY_PARTICLE = pygame.transform.scale(FRIENDLY_PARTICLE_IMAGE, (40, 40))
ENEMY1 = pygame.transform.scale(ENEMY1_IMAGE, (64, 64))

WAVE_LEN = 5
ENEMY_VEL = 2
PARTICLE_VEL = 5
LEVEL = 0
LIVES = 1
GAME_OVER = False
PAUSED = False
DEATH_ANIMATION = 0
EXIT_FLAG = False
RESET_FLAG = False