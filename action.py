class Action:
    def perform(self, engine, entity):
        # do this within the engine, entity performs the action
        # this raises an error and so Action must be overridden by one of the subclasses
        raise NotImplementedError()


# action when escape is pressed, exits program
class EscapeAction(Action):
    def perform(self, engine, entity):
        raise SystemExit()


# movement will take positional arguements, dx and dy, to handle player movement based on key inputs.
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine, entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        # don't move if movement will be out of bounds of game map
        if not engine.game_map.in_bounds(dest_x, dest_y):
            return
        
        # don't move if the destination tile is not walkable, i.e. a floor tile
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return

        entity.move(self.dx, self.dy) 
