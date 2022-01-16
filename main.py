import pygame
import random

import globals
import ship


WINDOW = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption(globals.CAPTION)
button = pygame.Rect(globals.WIDTH/2-50, globals.HEIGHT/2+50, 100, 40)
enemies = []

# Main game loop function
def main():
    while not globals.EXIT_FLAG:
        # Place player on centre of screen
        player = ship.Player(globals.WIDTH/2-globals.SPACESHIP_WIDTH, globals.HEIGHT/2-globals.SPACESHIP_HEIGHT)
        clock = pygame.time.Clock()
        globals.PAUSED = False 
        globals.DEATH_ANIMATION = 0
        print(f"clearing {len(enemies)} enemies")
        enemies.clear()
        run = True
        while run:  # Main game loop
            # Set FPS
            clock.tick(globals.FPS)

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    globals.EXIT_FLAG = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button.collidepoint(event.pos): # Restart the game quickly
                            globals.LIVES = 5
                            globals.RESET_FLAG = True
                            globals.GAME_OVER = False
                            globals.WAVE_LEN = 5
                            globals.LEVEL = 0
            
            # Draw the window
            draw_window(player)

            # Check RESET_FLAG
            if globals.RESET_FLAG:
                globals.RESET_FLAG = False
                run = False

            # Stop the game
            if globals.PAUSED:
                continue

            # Check if player lost
            if globals.LIVES <= 0:
                globals.GAME_OVER = True
                globals.PAUSED = True
        
            # Check if player was killed
            if player.dead:
                globals.PAUSED = True
                globals.LIVES += -1

            # Increment level when all enemies have been killed
            if len(enemies) == 0:
                globals.LEVEL += 1
                globals.WAVE_LEN += 1
                for i in range(globals.WAVE_LEN):
                    enemy = ship.Enemy(random.randrange(50, globals.WIDTH-50), random.randrange(-1500, -50), 1)
                    enemies.append(enemy)

            # Handle user input
            keys_pressed = pygame.key.get_pressed()
            handle_movement(keys_pressed, player)

            # Move enemies and make 'em shoot
            for enemy in enemies: # loop through copy of array
                enemy.move(globals.ENEMY_VEL)
                prob = round(globals.FPS*4/len(enemies))
                if random.randrange(0, prob) == 1:
                    enemy.shoot()
                if enemy.y + 64 > globals.HEIGHT: # Kill off-screen enemies
                    globals.LIVES -= 1
                    enemies.remove(enemy)

    
    print("Thanks for playing!")
    pygame.quit()

def draw_window(player):
    # Set a background image
    WINDOW.blit(globals.BACKGROUND, (0, 0))

    # Draw score
    lives_txt = globals.MAIN_FONT.render(f'LIVES', True, globals.WHITE)
    level_txt = globals.MAIN_FONT.render(f'LEVEL: {globals.LEVEL}', True, globals.WHITE)
    WINDOW.blit(level_txt, (globals.WIDTH-level_txt.get_width(), globals.HEIGHT-level_txt.get_height()))
    WINDOW.blit(lives_txt, (0, globals.HEIGHT-lives_txt.get_height()))
    for i in range(globals.LIVES):
        WINDOW.blit(globals.BLUE_SPACESHIP_SMOL, (lives_txt.get_width() + globals.BLUE_SPACESHIP_SMOL.get_width()*i + 20, globals.HEIGHT-lives_txt.get_height()-5))

    # Draw enemies
    for enemy in enemies:
        enemy.draw(WINDOW)
        # Move lasers and check if they hit the player.
        enemy.move_particles(globals.PARTICLE_VEL, player)

    # Draw the player
    if not player.dead:
        player.draw(WINDOW)
        player.move_particles(-globals.PARTICLE_VEL, enemies)
    else: # Player died, draw death animation
        if globals.DEATH_ANIMATION >= len(globals.EXPLOSION_SPRITE): # Finished displaying the animation
            globals.RESET_FLAG = True            
        else:
            img = globals.EXPLOSION_SPRITE[globals.DEATH_ANIMATION]
            WINDOW.blit(img, (player.x, player.y))
            globals.DEATH_ANIMATION += 1

    
    # GAME OVER
    if globals.GAME_OVER: # Show gameover text and dim the display
        lost_label = globals.DEATH_FONT.render("GAME OVER", 1, globals.WHITE)
        fade = pygame.Surface((globals.WIDTH, globals.HEIGHT), pygame.SRCALPHA)
        fade.fill((0, 0, 0, 150))
        WINDOW.blit(fade, (0,0))
        WINDOW.blit(lost_label, (globals.WIDTH/2 - lost_label.get_width()/2, globals.HEIGHT/2-lost_label.get_height()/2))
        pygame.draw.rect(WINDOW, globals.WHITE, button)
        retry_label = globals.MAIN_FONT.render("RETRY", 1, globals.PINK)
        WINDOW.blit(retry_label, (globals.WIDTH/2 - retry_label.get_width()/2, globals.HEIGHT/2+50))


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
            player.shoot()

# Only run if executed directly
if __name__ == "__main__":
    main()
