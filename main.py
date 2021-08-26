#!/usr/bin/env python3
from entity import Entity
import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    # setting size of terminal window to render in
    screen_width = 80
    screen_height = 50

    # importing tileset
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
        )

    event_handler = EventHandler()

    # create instances of Entity called player and npc
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    
    # set to store entities
    entities = {npc, player}

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike Tutorial",
        vsync=True,

    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        
        while True:
            # print player in terminal, uses player properites to get position etc.
            root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
