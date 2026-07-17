"""
MAIN GAME FILE

"""

import pygame
from . import game_settings
from . import player_module
from . import maploader

pygame.init()
clock = pygame.time.Clock()
current_map = "Villlage.tmx"
map = maploader.Map()

pygame.font.init()
font = pygame.font.SysFont(None, 30) # default pygame font :D

def main() -> None:
    """ Main function """
    DISPLAY = pygame.display.set_mode(game_settings.WINDOW_SIZE)

    player = player_module.Player(-200, -1300)

    map.load_map(current_map) # load the map

    run = True # be able to safely exit the loop
    while run:

        keys = pygame.key.get_pressed()
        player.handle_movement(keys, map.collision_rects)

        DISPLAY.fill((0,0,0))
        map.draw_map(DISPLAY, player.x, player.y)
        DISPLAY.blit(player.current_player_img,player.player_rect)

        # Debug
        for rect in map.collision_rects:
            pygame.draw.rect(DISPLAY, (255, 0, 0), rect.move(player.x, player.y), 2)
        pygame.draw.rect(DISPLAY, (255, 0, 0), player.hitbox.move(player.x, player.y), 2)

        DISPLAY.blit(font.render(f"FPS : {int(clock.get_fps())}", True, (0,0,0), (255,255,255)), (10, 10))
        DISPLAY.blit(font.render(f"x,y : {player.x} ; {player.y}", True, (0,0,0), (255,255,255)), (10, 35))

        pygame.display.update()
        clock.tick(game_settings.FPS)

        # let events process at the end in case of closing events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

main()

# Mira notes
# - moved keys handling to player_module
# + Added DISPLAY variable here
# - moved and rewritten collisions into player
# + addded Debug (font on screen, not console)