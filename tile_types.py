import numpy as np

# Tile graphics. dtype creates data type to be used by numpy.

graphic_dt = np.dtype(
    [
        ("ch", np.int32), # ch - character in int format, to be translated into unicode.
        ("fg", "3B"),  # fg - foreground colour, 3B - 3 unsigned bytes for RGB
        ("bg", "3B")   # bg - background colour
    ]
)

# Tile 'structure'
tile_dt = np.dtype(
    [ 
        ("walkable", np.bool), # true/false if tile can be walked over
        ("transparent", np.bool), # can be seen through
        ("dark", graphic_dt) # graphic for when not in field of vision
    ]
)

# * will enforce use of keywords so that parameter order doesn't matter
# function for defining individual tile types, returns an list for each tile
def new_tile(*, walkable, transparent, dark) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 100))
)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100))
)
