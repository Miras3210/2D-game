import pygame
import pytmx
from sys import exit

class Game:

    """General Game class for the game"""

    def __init__(self) -> None:
        """settings"""

        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60
        self.SCALE = 3
        self.TILE_SIZE = 48
        self.PLAYER_SPEED = 10
        self.current_map = "Assets/Villlage.tmx"
        pygame.display.set_caption("Panacea")


        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        

        #self.tmx_data = pytmx.load_pygame(self.current_map)
    def main(self) ->:
        """main game loop"""

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    pygame.quit()
                    exit()
        