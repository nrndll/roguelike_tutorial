#!/usr/bin/env python3
import tcod
from entity import Entity
from engine import Engine
from input_handlers import EventHandler
from game_map import GameMap

def main() -> None:
    # setting size of terminal window to render in
    screen_width = 80
    screen_height = 50

    # parameters of game map
    map_width = 80
    map_height = 45

    # importing tileset
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
        )
    
    # create instance of EventHandler class
    event_handler = EventHandler()

    # create instances of Entity called player and npc
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    
    # set to store entities, set enforces uniqueness. cant add entity more than once to set.
    entities = {npc, player}

    # create instance of GameMap class
    game_map = GameMap(map_width, map_height)

    # create instance of Engine class
    engine = Engine(entities, event_handler, game_map, player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike Tutorial",
        vsync=True,

    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        
        while True:
            # engine object takes root_console to render entities
            engine.render(root_console, context)
            # events stored in this variable, passed to engine object which will deal with them
            events = tcod.event.wait()
            engine.handle_events(events)
        

if __name__ == "__main__":
    main()
