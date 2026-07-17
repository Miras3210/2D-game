"""All game settings go here"""

from pathlib import Path as _Path

# Window config
WINDOW_WIDTH = 800 #windows width
WINDOW_HEIGHT = 400 #windows height
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) #windows size, tuple
FPS = 60 #frames per second of the game

# Map size config
TILE_SIZE = 48 #unit tile size of the game
SCALE = 3

# Player config
DEFAULT_PLAYER_SPEED = 5
DEFAULT_PLAYER_SIZE = 48

# Paths
ASSETS = _Path("Assets")


# Mira notes
# - Removed whole class since its like settings
# - removed window creation, it will be handled in the main file
# + added config for player