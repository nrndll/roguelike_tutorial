from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
from entity import Entity
from tcod.context import Context
from tcod.console import Console

class Engine:
    # entities:Set[Entity], event_handler:EventHandler, player:Entity
    def __init__(self, entities, event_handler, game_map, player):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self, events) -> None:
        # iterate through events, for each one carry out dispatch method
        for event in events:
            action = self.event_handler.dispatch(event)

            # do nothing if no action type
            if action is None:
                continue

            # if action is of the type MovementAction then move player entity via x and y
            elif isinstance(action, MovementAction):
                # if the tile the player is moving to has walkable attribute then move player
                if self.game_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
                    self.player.move(dx=action.dx, dy=action.dy)

            # if action is EscapeAction then close program
            elif isinstance(action, EscapeAction):
                raise SystemExit()

    # render all entites in console window
    def render(self, console, context) -> None:
        # draw game map in window
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)
        console.clear()