import pygame
import globals
from particle import Particle


class Ship:
    COOLDOWN_DUR = globals.FPS * 0.3

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.particle_image = None
        self.particles = []
        self.cooldown_counter = 0

    def draw(self, window):
        window.blit(self.ship_image, (self.x, self.y))
        for particle in self.particles:
            particle.draw(window)

    def move_particles(self, vel, obj):
        self.cooldown()
        for particle in self.particles[:]:
            particle.move(vel)
            if particle.off_screen():
                self.particles.remove(particle)
            elif particle.collision(obj):
                # Kill the player
                obj.dead = True
                self.particles.remove(particle)
    
    def cooldown(self):
        if self.cooldown_counter >= self.COOLDOWN_DUR:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def shoot(self):
        if self.cooldown_counter == 0:
            part = Particle(self.x, self.y, self.particle_image)
            self.particles.append(part)
            self.cooldown_counter = 1
    
    def get_width(self):
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = globals.BLUE_SPACESHIP
        self.particle_image = globals.FRIENDLY_PARTICLE
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health
        self.dead = False
    
    # Edit to check collision with enemies
    def move_particles(self, vel, objs):
        self.cooldown()
        for particle in self.particles[:]:
            particle.move(vel)
            if particle.off_screen():
                print("OFFSCREWEN!!")
                self.particles.remove(particle)
            else:
                for obj in objs:
                    if particle.collision(obj):
                        objs.remove(obj) # Remove the enemy from enemies
                        self.particles.remove(particle)

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
