#----------------------------------------------UNDER DEVELOPMENT----------------------------------------------

# Module is for Main code that works for all maps
# Dungeon = D, Floor = F

import pygame
import pytmx
from sys import exit

pygame.init()

class Player:
    """A class for the player"""
    def __init__(self):
        
        self.player_img = player_surf_down
        self.player_rect = self.player_img.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        self.camera_x = -150
        self.camera_y = -1050
        self.x = 0
        self.y = 0
        self.hitbox = pygame.Rect(self.player_rect.x + 10,self.player_rect.y + 18,28,28)

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.camera_y -= PLAYER_SPEED 
            self.y += PLAYER_SPEED 
            self.player_img = player_surf_down
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.camera_y += PLAYER_SPEED 
            self.y -= PLAYER_SPEED 
            self.player_img = player_surf_up
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.camera_x -= PLAYER_SPEED 
            self.x += PLAYER_SPEED 
            self.player_img = player_surf_right
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.camera_x += PLAYER_SPEED 
            self.x -= PLAYER_SPEED
            self.player_img = player_surf_left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.player_img, self.player_rect)

    def collision(self):

        # update hitbox position
        self.hitbox.topleft = (
            self.player_rect.x + 10,
            self.player_rect.y + 18
        )

        future_hitbox = self.hitbox.move(self.x, self.y)

        collision = False

        for rect in collision_rects:

            moved_rect = rect.move(self.camera_x, self.camera_y)

            if future_hitbox.colliderect(moved_rect):
                collision = True
                break

        return collision

def code():
    """Just a function to keep the code DRY"""
    for layer in tmx_data.visible_layers:
                if hasattr(layer, "tiles"):
                    for x, y, gid in layer:
                        tile = tmx_data.get_tile_image_by_gid(gid)
                        if tile:
                            tile = pygame.transform.scale(
                                tile,
                                (
                                    tmx_data.tilewidth * SCALE,
                                    tmx_data.tileheight * SCALE
                                )
                            )

                            screen.blit(
                                tile,
                                (
                                    x * tmx_data.tilewidth * SCALE + player.camera_x,
                                    y * tmx_data.tileheight * SCALE + player.camera_y
                                )
                            )
def display_map():
    """Logic to display the map"""
    if FIRST_FRAME == 0:
        code()
    else:
        code()

def main(CURRENT_MAP):
    """Main code and game loop"""
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        old_camera_x = player.camera_x
        old_camera_y = player.camera_y

        player.handle_keys()
        if player.collision():
            player.camera_x = old_camera_x
            player.camera_y = old_camera_y

        screen.fill((0, 0, 0))
        player.x = 0
        player.y = 0

        # print(player.player_rect.topleft,player.player_rect.topright,player.player_rect.bottomright,player.player_rect.bottomleft)

        # BLTTING AND DRAWING
        
        display_map() #To blit the tmx map
        player.draw(screen) # To blit the player 

        pygame.display.update()

        clock.tick(FPS)
        FIRST_FRAME = 1
        print(player.camera_x,player.camera_y)

# CONSTANTS

WIDTH = 800
HEIGHT = 600
FPS = 60
SCALE = 3
CURRENT_MAP = "Assets/Villlage.tmx"
TILE_SIZE = 48
FIRST_FRAME = 0
PLAYER_SPEED = 5
MAPS = { "Village" :{"Background" :"Assets/Villlage.tmx",
                      "Doors" : [{"rect": pygame.Rect()
                                  "target" : "Dungeon_Ground_Floor"
                                  "spawn"  : ()}]}

        "Dungeon_Ground_Floor" : "Assets/revised_ground_floor_map.tmx",
        "Dungeon_Floor_1" : "Empty",
        "Dungeon_Floor_2" : "Empty",
        "Dungeon_Floor_3" : "Empty",
        "Dungeon_Floor_4" : "Empty",
        "Dungeon_Floor_5" : "Empty"
        }

# WINDOW GENERATION

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Panacea")

# 

clock = pygame.time.Clock()

# LOAD MAP

tmx_data = pytmx.load_pygame(CURRENT_MAP)

# PLAYER IMAGE LOAD AND RESIZE

PLAYER_SIZE = 48

player_up = pygame.image.load("Assets/player-up.png").convert_alpha()
player_down = pygame.image.load("Assets/player-down.png").convert_alpha()
player_left = pygame.image.load("Assets/player-left.png").convert_alpha()
player_right = pygame.image.load("Assets/player-right.png").convert_alpha()

player_surf_up = pygame.transform.scale(player_up, (PLAYER_SIZE, PLAYER_SIZE))
player_surf_down = pygame.transform.scale(player_down, (PLAYER_SIZE, PLAYER_SIZE))
player_surf_left = pygame.transform.scale(player_left, (PLAYER_SIZE, PLAYER_SIZE))
player_surf_right = pygame.transform.scale(player_right, (PLAYER_SIZE, PLAYER_SIZE))

# COLLISION SYSTEM

collision_rects = []

for layer in tmx_data.visible_layers:
    if layer.name == "Collision layer":
        for x, y, gid in layer:
            if gid != 0:
                rect = pygame.Rect(
                    x * tmx_data.tilewidth * SCALE,
                    y * tmx_data.tileheight * SCALE,
                    tmx_data.tilewidth * SCALE,
                    tmx_data.tileheight * SCALE
                )
                collision_rects.append(rect)

# MAKING A PLAYER OBJECT
player = Player()

main(CURRENT_MAP)