import pygame
import random

import globals
import ship


WINDOW = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption(globals.CAPTION)

enemies = []

# Main game loop function
def main():
    # Place player on centre of screen
    player = ship.Player(globals.WIDTH/2-globals.SPACESHIP_WIDTH, globals.HEIGHT/2-globals.SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True

    while run:  # Main game loop
        # Set FPS
        clock.tick(globals.FPS)

        # Draw the window
        draw_window(player)

        # Check if player lost
        if globals.LIVES <= 0 or player.health <= 0:
            globals.GAME_OVER = True
            globals.GAME_OVER_COUNT += 1

        # Stop the game
        if globals.GAME_OVER:
            if globals.GAME_OVER_COUNT > globals.FPS * 5:
                run = False
            else:
                continue

        # Increment level when all enemies have been killed
        if len(enemies) == 0:
            globals.LEVEL += 1
            globals.WAVE_LEN += 1
            for i in range(globals.WAVE_LEN):
                enemy = ship.Enemy(random.randrange(50, globals.WIDTH-50), random.randrange(-1500, -50), 1)
                enemies.append(enemy)
            
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Handle user input
        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, player)

        # Move enemies
        for enemy in enemies[:]: # loop through copy of array
            enemy.move(globals.ENEMY_VEL)
            if enemy.y + 64 > globals.HEIGHT: # Kill off-screen enemies
                globals.LIVES -= 1
                enemies.remove(enemy)

    print("Thanks for playing!")
    pygame.quit()

def draw_window(player):
    # Set a background image
    WINDOW.blit(globals.BACKGROUND, (0, 0))
    WINDOW.blit(globals.FRIENDLY_PARTICLE, (200, 200))

    # Draw score
    img = globals.MAIN_FONT.render(f'lives: {globals.LIVES}', True, globals.WHITE)
    WINDOW.blit(img, (0, 0))

    # Draw enemies
    for enemy in enemies: 
        enemy.draw(WINDOW)

    # Draw the player
    player.draw(WINDOW)
    if globals.GAME_OVER: # Show gameover text and dim the display
        lost_label = globals.DEATH_FONT.render("GAME OVER", 1, globals.WHITE)
        fade = pygame.Surface((globals.WIDTH, globals.HEIGHT), pygame.SRCALPHA)
        fade.fill((0, 0, 0, 150))
        WINDOW.blit(fade, (0,0))
        WINDOW.blit(lost_label, (globals.WIDTH/2 - lost_label.get_width()/2, globals.HEIGHT/2-lost_label.get_height()/2))

    # Update the display
    pygame.display.update()

def handle_movement(keys_pressed, player):
        if keys_pressed[pygame.K_w]: # UP
            if player.y > 0:
                player.y += -globals.VELOCITY
        if keys_pressed[pygame.K_s]: # DOWN
            if player.y < globals.HEIGHT-globals.SPACESHIP_HEIGHT:
                player.y += globals.VELOCITY
        if keys_pressed[pygame.K_a]: # LEFT
            if player.x > 10:
                player.x += -globals.VELOCITY
        if keys_pressed[pygame.K_d]: # RIGHT
            if player.x < globals.WIDTH-globals.SPACESHIP_WIDTH:
                player.x += globals.VELOCITY
        if keys_pressed[pygame.K_SPACE]: # SPACE
            print()

# Only run if executed directly
if __name__ == "__main__":
    main()
