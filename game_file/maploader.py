import pygame
import pytmx
from . import game_settings

class Map: #checked but probably has that collision bug
    """Everything map related"""
    def __init__(self) -> None:
        self.collision_rects: list[pygame.Rect] = []
        self.tmx_data: pytmx.TiledMap

    def load_map(self, mapname: str):
        self.tmx_data = pytmx.load_pygame(str(game_settings.ASSETS / mapname))
        self.collision_rect_maker()

    def collision_rect_maker(self) -> None:
        """makes collision rects"""
        self.collision_rects: list[pygame.Rect] = []
        for layer in self.tmx_data.visible_layers:
            if layer.name == "Collision layer":
                for x, y, gid in layer:
                    if gid != 0:
                        rect = pygame.Rect(x * self.tmx_data.tilewidth * game_settings.SCALE, y * self.tmx_data.tileheight * game_settings.SCALE, self.tmx_data.tilewidth * game_settings.SCALE, self.tmx_data.tileheight * game_settings.SCALE)
                        self.collision_rects.append(rect)

    def draw_map(self, surface: pygame.Surface, camera_x : int, camera_y : int) -> None:
        """blits the map to the display surface"""
        # we add culling in order to only display what we can see
        tw = self.tmx_data.tilewidth * game_settings.SCALE
        th = self.tmx_data.tileheight * game_settings.SCALE
        # tile range visible on screen
        start_x = max(0, -camera_x // tw)
        start_y = max(0, -camera_y // th)
        end_x = min(self.tmx_data.width,  start_x + game_settings.WINDOW_WIDTH  // tw + 2)
        end_y = min(self.tmx_data.height, start_y + game_settings.WINDOW_HEIGHT // th + 2)

        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, "tiles"):
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        gid = layer.data[y][x]
                        tile = self.tmx_data.get_tile_image_by_gid(gid)
                        if tile:
                            tile = pygame.transform.scale(tile, (tw, th))
                            surface.blit(tile, (x * tw + camera_x, y * th + camera_y))

    def del_map_rect(self) -> None:
        """deletes all the present rects of the map"""
        self.collision_rects.clear()

# Mira notes
# + small change to map loading
# + map culling (rendering only what you can see)