#----------------------------------------------UNDER DEVELOPMENT---------------------------------------------------------------------

import pygame
import pytmx
from sys import exit

pygame.init()

class Player:
    def __init__(self,xx,yy):
        
        self.player_img = player_surf_down
        self.player_rect = self.player_img.get_rect(center = (xx,yy))
        self.x = 0
        self.y = 0
        self.hitbox = pygame.Rect(self.player_rect.x + 10,self.player_rect.y + 18,28,24)

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.y += 3
            self.player_img = player_surf_down
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.y -= 3
            self.player_img = player_surf_up
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.x += 3
            self.player_img = player_surf_right
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.x -= 3
            self.player_img = player_surf_left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.player_img, self.player_rect)

    def collision(self):
        
        future_hitbox = self.hitbox.move(self.x, self.y)

        collision = False

        for rect in collision_rects:
            if future_hitbox.colliderect(rect):
                collision = True
                break

        if not collision:

            self.player_rect.centery += self.y
            self.player_rect.centerx += self.x
            self.hitbox.x = self.player_rect.x + 10
            self.hitbox.y = self.player_rect.y + 18



#Dungeon = D, Floor = F

# ---------------- SETTINGS ----------------

WIDTH = 800
HEIGHT = 600
FPS = 60
SCALE = 3
CURRENT_MAP = "Assets/Villlage.tmx"
TILE_SIZE = 48

# ---------------- WINDOW GENERATION----------------

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Panacea")
clock = pygame.time.Clock()

# ---------------- LOAD MAP ----------------
tmx_data = pytmx.load_pygame(CURRENT_MAP)

# ---------------- PLAYER IMAGE LOAD AND RESIZE ----------------
PLAYER_SIZE = 48

player_up = pygame.image.load("Assets/player-up.png").convert_alpha()
player_down = pygame.image.load("Assets/player-down.png").convert_alpha()
player_left = pygame.image.load("Assets/player-left.png").convert_alpha()
player_right = pygame.image.load("Assets/player-right.png").convert_alpha()

player_surf_up = pygame.transform.scale(player_up, (PLAYER_SIZE, PLAYER_SIZE))
player_surf_down = pygame.transform.scale(player_down, (PLAYER_SIZE, PLAYER_SIZE))
player_surf_left = pygame.transform.scale(player_left, (PLAYER_SIZE, PLAYER_SIZE))
player_surf_right = pygame.transform.scale(player_right, (PLAYER_SIZE, PLAYER_SIZE))

# ---------------- COLLISION SYSTEM ----------------

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
player = Player(750,350)
# ---------------- GAME LOOP ----------------
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.handle_keys()

    player.collision()
    player.x = 0
    player.y = 0
    # print(player.player_rect.topleft,player.player_rect.topright,player.player_rect.bottomright,player.player_rect.bottomleft)

    # -------- DRAW --------
    screen.fill((0, 0, 0))

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
                            x * tmx_data.tilewidth * SCALE,
                            y * tmx_data.tileheight * SCALE
                        )
                    )
    player.draw(screen)
    
    print(player.player_rect.center)

    pygame.display.update()
    clock.tick(FPS)
#this might go in __init__.py