from tile import world
from player import p

alive = True

"""
Game loop:
---------

1. Print tile description
2. Get available actions
3. Ask input
4. Parse input
"""
while alive:
    # Check player position and print tile description
    print(p.get_tile(world))

    # Reset list of available actions each tile/iteration
    p.available_actions = []
    p.get_adjacent_tiles(world)

    # print("\n--------------\nAvailable actions:\n")
    # for action in p.available_actions:
    #     print(action.name)

    # TODO If there is no action found, print a statement saying so.
    # TODO Split the user input into keywords

    user_input = input("What would you like to do?\n> ").lower()

    if user_input == "stop":
        alive = False
        break

    for action in p.available_actions:
        if user_input in action.hotkey:
            action.function()
            break