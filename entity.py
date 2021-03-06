# this will be a generic class to handle all entities in game, i.e. player, enemies, items etc.

class Entity:
    # tutorial defines parameters types e.g. x:int, y:int, char:str, color:Tuple[int,int,int]
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    # increments x and y axis positions to move entity
    def move(self, dx, dy) -> None:
        self.x += dx
        self.y += dy