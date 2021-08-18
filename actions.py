class Action:
    pass

# action when escape is pressed
class EscapeAction(Action):
    pass


# movement will take positional arguements, dx and dy, to handle player movement based on key inputs.
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy