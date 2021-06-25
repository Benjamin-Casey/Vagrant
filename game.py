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
def main():
    alive = True

    while alive:
        player_tile = p.get_tile(world)

        # Check player position and print tile description
        print(player_tile)

        # Reset list of available actions each tile/iteration
        p.available_actions = []
        p.get_adjacent_tiles(world)
        p.get_actions(player_tile)

        # print("\n--------------\nAvailable actions:\n")
        # for action in p.available_actions:
        #     print(action.name)

        # TODO If there is no action found, print a statement saying so.
        # TODO Split the user input into keywords?

        user_input = input("What would you like to do?\n> ").lower()

        if user_input == "stop":
            alive = False
            break

        # NOTE: this doesn't allow for params (bad system)
        # TODO change: if action has param: action.function(param)
        for action in p.available_actions:
            if user_input.split()[0] in action.hotkey:
                # TODO fix this shit
                if action.name == "Take Item":
                    action.function(user_input.split()[1], player_tile)

                else:
                    action.function()
                break

if __name__ == "__main__":
    main()