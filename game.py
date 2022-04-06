from operator import itemgetter
from player import Player
from world_map import TileMap, WORLD_MAP


# NOTE: consider moving this to another file
class InputHandler:
    def __init__(self, player, w_map):
        self.inp = None
        self.player = player
        self.w_map = w_map

    def get_input(self):
        self.inp = input("What would you like to do?\n> ").lower()

    def perform_action(self):
        # NOTE: Can change the keyword checking after change with a list from an Action object.
        match self.inp.split():
            case ['go', ('north' | 'south' | 'east' | 'west') as direction]:
                # Get adjacent tiles
                if direction in self.w_map.adjacent_tiles(player):
                    player.move(direction)
                else:
                    print("Cannot move that way...\n")

            # TODO: Fix having to capitalize the items. This will probably come with item objects instead of strings.
            case ['take', item]:
                # Check if the item is on the tile. To do this, get the tile the player is on.
                p_tile = self.w_map.locate_object(player)
                if item.capitalize() in p_tile.items:
                    # TODO: make this a player function.
                    player.inventory.append(item)
                    p_tile.items.remove(item.capitalize())

            case ['inventory'] | ['check', 'inventory']:
                if player.inventory:
                    player.print_inventory()
                else:
                    print("You have no items in your inventory!")

            case ['break']:
                # Kill player to end the loop.
                print("Breaking loop by killing player. InputHandler function.")
                player.hp = 0


class Game:
    def __init__(self):
        pass

    def run(self, player, w_map):

        i_handler = InputHandler(player, w_map)
        while player.is_alive:
            # Print the tile information to the player
            player_location = w_map.locate_object(player)
            print(f"---\n{player_location}")

            # Ask for and handle the players input
            i_handler.get_input()
            i_handler.perform_action()


if __name__ == "__main__":
    # Create player
    player = Player()

    # Init map
    world_map = TileMap()
    world_map.generate_map(WORLD_MAP)

    # Set players starting position
    player_starting_location = world_map.player_start
    player.set_location(player_starting_location.x, player_starting_location.y)

    # Init and run game
    game = Game()
    game.run(player, world_map)
