# main code
# gets imported when u do import Game_file in run_game.py
print("the module is running")
#----------------------------------------------UNDER DEVELOPMENT---------------------------------------------------------------------
import pygame
import pytmx
import pyscroll
from sys import exit

pygame.init()

#Entry/Exit coordinates
#Dungeon = D, Floor = F

# ---------------- SETTINGS ----------------
WIDTH = 400
HEIGHT = 300
FPS = 60

SCALE = 3
PLAYER_SPEED = 3

CURRENT_MAP = "Assets/Villlage.tmx"

# ---------------- WINDOW ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game_name")

clock = pygame.time.Clock()

# ---------------- LOAD MAP ----------------
tmx_data = pytmx.load_pygame(CURRENT_MAP)

# ---------------- Make the scrolling layer ---------------- 
screen_size = (400, 300)
map_data = pyscroll.TiledMapData(tmx_data)
map_layer = pyscroll.BufferedRenderer(map_data, screen_size)
group = pyscroll.PyscrollGroup(map_layer=map_layer)


# ---------------- LOAD PLAYER ----------------
playerup = pygame.image.load("Assets/player-up.png").convert_alpha()
playerdown = pygame.image.load("Assets/player-down.png").convert_alpha()
playerleft = pygame.image.load("Assets/player-left.png").convert_alpha()
playerright = pygame.image.load("Assets/player-right.png").convert_alpha()

# Scale player sprites
PLAYER_SIZE = 48

playerup = pygame.transform.scale(playerup, (PLAYER_SIZE, PLAYER_SIZE))
playerdown = pygame.transform.scale(playerdown, (PLAYER_SIZE, PLAYER_SIZE))
playerleft = pygame.transform.scale(playerleft, (PLAYER_SIZE, PLAYER_SIZE))
playerright = pygame.transform.scale(playerright, (PLAYER_SIZE, PLAYER_SIZE))

# Current player image
player = playerdown

# ---------------- PLAYER RECT ----------------
playerrect = player.get_rect(center=(400, 300))

# Smaller collision hitbox
hitbox = pygame.Rect(
    playerrect.x + 10,
    playerrect.y + 18,
    28,
    24
)
player_sprite = pygame.sprite.Sprite()
player_sprite.image = playerdown
player_sprite.rect = playerrect
group.add(player_sprite)

(800, 600)

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
# ---------------- GAME LOOP ----------------
while True:

    # -------- EVENTS --------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # -------- INPUT --------
    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dy = -PLAYER_SPEED
        player = playerup

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED
        player = playerdown

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED
        player = playerleft

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED
        player = playerright

    # -------- COLLISION AND MOVEMENT --------
    future_hitbox = hitbox.move(dx, dy)

    blocked = False

    for rect in collision_rects:

        if future_hitbox.colliderect(rect):
            blocked = True
            break

    if not blocked:
        player_sprite.rect.get_rect(center=(400+dx, 300+dy))
        hitbox.y += dy
        hitbox.x += dx


    # -------- DRAW --------
    screen.fill((0, 0, 0))

    # Draw player and center the camera angle on the player
    group.center(player_sprite.rect.center)
    group.draw(screen)

    # ---------------- DEBUG ----------------
    # Show collision boxes

    # for rect in collision_rects:
    #     pygame.draw.rect(screen, (255, 0, 0), rect, 2)

    # Show player hitbox

    # pygame.draw.rect(screen, (0, 255, 0), hitbox, 2)
    print(playerrect.center)

    pygame.display.update()
    clock.tick(FPS)
#this might go in __init__.py