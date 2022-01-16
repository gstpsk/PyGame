import pygame
import globals


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.particle_image = None
        self.particles = []
        self.cooldown = 0

    def draw(self, window):
        window.blit(self.ship_image, (self.x, self.y))
        #pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, globals.SPACESHIP_WIDTH, globals.SPACESHIP_WIDTH))


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = globals.BLUE_SPACESHIP
        self.particle_image = globals.FRIENDLY_PARTICLE
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health


class Enemy(Ship):
    TYPE_MAP = {
        1: (globals.ENEMY1, globals.FRIENDLY_PARTICLE),
        #2: (globals.ENEMY2, globals.FRIENDLY_PARTICLE)
    }

    def __init__(self, x, y, type, health=100):
        super().__init__(x, y, health)
        self.ship_image, self.particle_image = self.TYPE_MAP[type]
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health
    
    def move(self, vel):
        self.y += vel
    
    def get_height():
        return self.ship_image.get_height()
