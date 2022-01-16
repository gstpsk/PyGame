import pygame
import globals
import ship


WINDOW = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption(globals.CAPTION)

# Main game loop function
def main():
    # Place player on centre of screen
    player = ship.Player(globals.WIDTH/2-globals.SPACESHIP_WIDTH, globals.HEIGHT/2-globals.SPACESHIP_HEIGHT,)

    clock = pygame.time.Clock()
    run = True
    while run:  # Main game loop
        clock.tick(globals.FPS)
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Handle user input
        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, player)

        
        draw_window(player)
        #player.draw(WINDOW)
        #pygame.display.update()
    print("Thanks for playing!")
    pygame.quit()

def draw_window(player):
    # Set a background image
    WINDOW.blit(globals.BACKGROUND, (0, 0))
    WINDOW.blit(globals.FRIENDLY_PARTICLE, (200, 200))
    # Draw the player
    player.draw(WINDOW)
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
