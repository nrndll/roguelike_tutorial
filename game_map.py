import numpy as np
from numpy.lib.shape_base import tile
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width, height):
        self.width, self.height = width, height

        # uses numpy to return an array of given size and type, filled with fill_value
        # in this case the array will use the width and height parameters from the initialiser and will be filled with floor tiles.
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")
        self.tiles[30:33, 22] = tile_types.wall
    
    # returns true as long as x and y are within the map, prevents player going beyond the boundaries
    def in_bounds(self, x, y) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    # uses tiles_rgb method of Console to render map quickly
    def render(self, console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]