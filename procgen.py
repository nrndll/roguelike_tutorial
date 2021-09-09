import random
import tcod
from game_map import GameMap
import tile_types

class RectangularRoom:
    # calculates position of bottom right corner by taking x + y position of top left corner, the width and height
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    # @property is a decorator to set the property "centre" being defined in this method.
    # centre will return the centre position of the room. 
    @property
    def centre(self):
        centre_x = int((self.x1 + self.x2) / 2)
        centre_y = int((self.y1 + self.y2) / 2)

        return centre_x, centre_y

    # this is setting the inner room, i.e. the room that will be carved out of wall tiles and become floor tiles.
    # the x and y axis are both 2 dimensional arrays so it is returning slices from each axis to get inner x + y coordinates.
    @property
    def inner(self):
        # the +1 here is to ensure that additional rooms will be separated by walls, without it the rooms would overlap with walkable tiles.
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

# generate an L-shaped tunnel between two points/rooms. takes two tuples of x+y coordinates
def tunnel_between(start, end):
    x1, y1 = start
    x2, y2 = end

# 50/50 chance for one or the other 
    if random.random() < 0.5:
        # horizontal then vertical
        corner_x, corner_y = x2, y1

    else:
        # vertical then horizontal
        corner_x, corner_y = x1, y2
    
    # generating coordinates for the tunnel, bresenham part of line of sight tcod module. In this case used to draw the two lines, takes a start and an end point as arguments, then converted to list.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        # yield expression returns a generator function rather than just returning the values. The generator can be suspended and retain local state, to be resumed at another point when one of it's methods are called e.g. __next__() resumes with last yield expression and continues from where it had stopped.
        yield x, y

    #  so this will create a list of x + y coords using the given corner and starting points, iterating through them, yielding x + y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y


def generate_dungeon(map_width, map_height):
    dungeon = GameMap(map_width, map_height)

    room1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room1.inner] = tile_types.floor
    dungeon.tiles[room2.inner] = tile_types.floor

    for x,y in tunnel_between(room2.centre, room1.centre):
        dungeon.tiles[x, y] = tile_types.floor

    return dungeon
