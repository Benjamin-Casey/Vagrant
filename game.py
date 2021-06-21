from tile import tiles
from player import p
from actions import actions

alive = True

while alive:
    # Check player position and print tile description
    print(p.get_tile(tiles))
    user_input = input("What would you like to do?\n> ")

    # Break loop at 'stop'
    if user_input.lower() == "stop":
        alive = False
        break

    # TODO If there is no action found, print a statement saying so.
    for action in actions:
        if user_input.lower() in action.hotkey:
            action.function()
            break