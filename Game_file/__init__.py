#----------------------------------------------UNDER DEVELOPMENT----------------------------------------------

# Module is for Main code that works for all maps
# Dungeon = D, Floor = F

import pygame
import pytmx
from sys import exit

pygame.init()
class Game:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60
        self.SCALE = 3
        self.CURRENT_MAP = "Assets/Villlage.tmx"
        self.TILE_SIZE = 48
        self.PLAYER_SPEED = 10
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Panacea")
        self.tmx_data = pytmx.load_pygame(self.CURRENT_MAP)
        self.player = Player(self)
        self.collision_rects = []
        self.door_rects = []
        self.collision()
        self.door()

    def Door_event(self):
        pygame.time.delay(150)
        EVENT = 0
        for door in self.door_rects:
            moved_rect = door["rect"].move(self.player.camera_x, self.player.camera_y)

            if self.player.hitbox.colliderect(moved_rect):
                print("check")
                self.CURRENT_MAP = door["target"]
                print(self.CURRENT_MAP)

                self.player.camera_x = door["spawn_x"]
                self.player.camera_y = door["spawn_y"]
                EVENT = 1
        return EVENT

    def collision(self):
        self.collision_rects = []
        for layer in self.tmx_data.visible_layers:
            if layer.name == "Collision layer":
                for x, y, gid in layer:
                    if gid != 0:
                        rect = pygame.Rect(
                            x * self.tmx_data.tilewidth * self.SCALE,
                            y * self.tmx_data.tileheight * self.SCALE,
                            self.tmx_data.tilewidth * self.SCALE,
                            self.tmx_data.tileheight * self.SCALE
                        )
                        self.collision_rects.append(rect)
    def door(self):
        self.door_rects = []
        for obj in self.tmx_data.get_layer_by_name("Door Layer"):

            door_rect = pygame.Rect(
            obj.x * self.SCALE,
            obj.y * self.SCALE,
            obj.width * self.SCALE,
            obj.height * self.SCALE
            )
            target_map = obj.properties["target"]

            spawn_x = obj.properties["spawn_x"]
            spawn_y = obj.properties["spawn_y"]

            self.door_rects.append({
                "rect": door_rect,
                "target": target_map,
                "spawn_x": spawn_x,
                "spawn_y" : spawn_y
            })
    
    def draw_map(self):
        """Just a function to keep the code DRY"""
        for layer in self.tmx_data.visible_layers:
                    if hasattr(layer, "tiles"):
                        for x, y, gid in layer:
                            tile = self.tmx_data.get_tile_image_by_gid(gid)
                            if tile:
                                tile = pygame.transform.scale(
                                    tile,
                                    (
                                        self.tmx_data.tilewidth * self.SCALE,
                                        self.tmx_data.tileheight * self.SCALE
                                    )
                                )

                                self.screen.blit(
                                    tile,
                                    (
                                        x * self.tmx_data.tilewidth * self.SCALE + self.player.camera_x,
                                        y * self.tmx_data.tileheight * self.SCALE + self.player.camera_y
                                    )
                                )
    def display_map(self):
        self.draw_map()


    def main(self):
        """Main code and game loop"""
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            old_camera_x = self.player.camera_x
            old_camera_y = self.player.camera_y

            self.player.handle_keys()
            collided = self.player.collision()
            if collided:
                self.player.camera_x = old_camera_x
                self.player.camera_y = old_camera_y
            event = self.Door_event()
            if event == 1:
                self.tmx_data = pytmx.load_pygame(self.CURRENT_MAP)

                self.collision()
                self.door()

            self.screen.fill((0, 0, 0))
            self.player.x = 0
            self.player.y = 0

            # print(player.player_rect.topleft,player.player_rect.topright,player.player_rect.bottomright,player.player_rect.bottomleft)

            # BLTTING AND DRAWING
            
            self.display_map() #To blit the tmx map
            self.player.draw() # To blit the player 

            pygame.display.update()

            self.clock.tick(self.FPS)
            # print(player.camera_x,player.camera_y)
            event = 0

class Player:
    """A class for the player"""
    def __init__(self, game):
        self.game = game
        self.PLAYER_SIZE = 48
        self.player_up = pygame.image.load("Assets/player-up.png").convert_alpha()
        self.player_down = pygame.image.load("Assets/player-down.png").convert_alpha()
        self.player_left = pygame.image.load("Assets/player-left.png").convert_alpha()
        self.player_right = pygame.image.load("Assets/player-right.png").convert_alpha()
        self.player_surf_up = pygame.transform.scale(self.player_up, (self.PLAYER_SIZE, self.PLAYER_SIZE))
        self.player_surf_down = pygame.transform.scale(self.player_down, (self.PLAYER_SIZE, self.PLAYER_SIZE))
        self.player_surf_left = pygame.transform.scale(self.player_left, (self.PLAYER_SIZE, self.PLAYER_SIZE))
        self.player_surf_right = pygame.transform.scale(self.player_right, (self.PLAYER_SIZE, self.PLAYER_SIZE))
        self.player_img = self.player_surf_down 
        self.player_rect = self.player_img.get_rect(center = (game.WIDTH // 2, game.HEIGHT // 2))
        self.camera_x = -150
        self.camera_y = -1050
        self.x = 0
        self.y = 0
        self.hitbox = pygame.Rect(self.player_rect.x + 10,self.player_rect.y + 18,28,28)
         

    def draw(self):
        """ Draw on surface """
        # blit yourself at your current position
        self.game.screen.blit(self.player_img, self.player_rect)

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.camera_y -= self.game.PLAYER_SPEED 
            self.y += self.game.PLAYER_SPEED 
            self.player_img = self.player_surf_down
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.camera_y += self.game.PLAYER_SPEED 
            self.y -= self.game.PLAYER_SPEED 
            self.player_img = self.player_surf_up
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.camera_x -= self.game.PLAYER_SPEED 
            self.x += self.game.PLAYER_SPEED 
            self.player_img = self.player_surf_right
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.camera_x += self.game.PLAYER_SPEED 
            self.x -= self.game.PLAYER_SPEED
            self.player_img = self.player_surf_left

    def collision(self):

        # update hitbox position
        self.hitbox.topleft = (
            self.player_rect.x + 10,
            self.player_rect.y + 18
        )

        future_hitbox = self.hitbox.move(self.x, self.y)

        collision = False

        for rect in self.game.collision_rects:

            moved_rect = rect.move(self.camera_x, self.camera_y)

            if future_hitbox.colliderect(moved_rect):
                collision = True
                break
        return collision


game = Game()
game.main()
