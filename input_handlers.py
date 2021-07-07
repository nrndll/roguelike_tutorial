# optional just denotes something that can be set to None
from typing import Optional

# importing tcod's event system
import tcod.event

# importing the action class with subclasses from action.py
from actions import Action, EscapeAction, MovementAction

# creating a class called EventHandler as a subclass of tcod.EventDispatch. This is a class that can direct events to the appropriate method.
class EventHandler(tcod.event.EventDispatch[Action]):
    
    # ev_quit is a method in EventDispatch, the following code overrides ev_quit so that SystemExit() will be called when a quit event is received.
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

# method that take key press events and return Action or None
def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
    
    # action variable holds the Action subclass that has been assigned. Without a valid key this will remain None.
    action: Optional[Action] = None

    # key variable that holds the key press
    key = event.sym

# conditions taking key input for up, down, left and right. Changes position.
    if key == tcod.event.K_UP:
        action = MovementAction(dx=0, dy=-1)
    elif key == tcod.event.K_DOWN:
        action = MovementAction(dx=0, dy=1)
    elif key == tcod.event.K_LEFT:
        action = MovementAction(dx=-1, dy=0)
    elif key == tcod.event.K_RIGHT:
        action = MovementAction(dx=1, dy=0)
    
    elif key == tcod.event.K_ESCAPE:
        action = EscapeAction()

    # no valid key input:
    return Action