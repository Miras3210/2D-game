import pygame
from . import game_settings

class Player:#checked
    """ Player class """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.size = game_settings.DEFAULT_PLAYER_SIZE
        self.speed = game_settings.DEFAULT_PLAYER_SPEED

        #assets loading and transformation
        assets = game_settings.ASSETS

        self.player_surf_up = pygame.transform.scale(pygame.image.load(assets / "player-up.png"), (self.size, self.size))
        self.player_surf_down = pygame.transform.scale(pygame.image.load(assets / "player-down.png"), (self.size, self.size))
        self.player_surf_left = pygame.transform.scale(pygame.image.load(assets / "player-left.png"), (self.size, self.size))
        self.player_surf_right = pygame.transform.scale(pygame.image.load(assets / "player-right.png"), (self.size, self.size))
        self.current_player_img = self.player_surf_down

        #player position control and hitbox rect
        self.player_rect = self.current_player_img.get_rect()
        self.player_rect.center = (game_settings.WINDOW_WIDTH/2, game_settings.WINDOW_HEIGHT/2)

        self.hitbox = pygame.Rect(
            game_settings.WINDOW_WIDTH // 2 - self.size // 2 + 10 - self.x,
            game_settings.WINDOW_HEIGHT // 2 - self.size // 2 + 18 - self.y,
            28, 28
        )

    def player_hitbox_move(self, del_x : int, del_y : int) -> None:
        """move the player hitbox"""
        self.hitbox = self.hitbox.move(del_x, del_y)

    def handle_movement(self, keys: pygame.key.ScancodeWrapper, collision_rects: list[pygame.Rect]):
        """ Handles Keys """
        lastpos = (self.x,self.y)

        # calculate delta using a shortcut to avoid if conditions
        delta_y = self.speed * ((keys[pygame.K_w] or keys[pygame.K_UP]) - (keys[pygame.K_s] or keys[pygame.K_DOWN]))
        delta_x = self.speed * ((keys[pygame.K_a] or keys[pygame.K_LEFT]) - (keys[pygame.K_d] or keys[pygame.K_RIGHT]))
        
        # uncomment if you want previous code
        # if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        #     self.y -= self.speed
        #     # self.current_player_img = self.player_surf_down
        # if keys[pygame.K_w] or keys[pygame.K_UP]:
        #     self.y += self.speed
        #     # self.current_player_img = self.player_surf_up
        # if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        #     self.x -= self.speed
        #     # self.current_player_img = self.player_surf_right
        # if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        #     self.x += self.speed
        #     # self.current_player_img = self.player_surf_left

        # delta_x, delta_y = (self.x - lastpos[0], self.y - lastpos[1])
        
        # smooth 45° turns
        if delta_y: delta_x = int(delta_x * 0.8)
        if delta_x: delta_y = int(delta_y * 0.8)

        self.x += delta_x
        self.y += delta_y

        # skin choice
        if delta_x > 0:   self.current_player_img = self.player_surf_left
        elif delta_x < 0: self.current_player_img = self.player_surf_right
        elif delta_y > 0: self.current_player_img = self.player_surf_up
        else:             self.current_player_img = self.player_surf_down

        # separate X and Y collisions (make it smooth)
        # you can uncomment the code bellow to calculate it only once
        if delta_x:
            self.player_hitbox_move(-delta_x, 0)
            check = self.hitbox.collidelist(collision_rects)
            if check != -1:
                self.player_hitbox_move(delta_x, 0)
                self.x = lastpos[0]
        if delta_y:
            self.player_hitbox_move(0, -delta_y)
            check = self.hitbox.collidelist(collision_rects)
            if check != -1:
                self.player_hitbox_move(0, delta_y)
                self.y = lastpos[1]
        # if delta_x or delta_y:
        #     self.player_hitbox_move(-delta_x, -delta_y)
        #     check = self.hitbox.collidelist(collision_rects)
        #     if check != -1:
        #         self.player_hitbox_move(delta_x, delta_y)
        #         self.x, self.y = lastpos

        return

# Mira notes:
# + revamped player class
# - re-did asset loading
# + added movement handling here
# + added optimized collisions