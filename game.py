from player import Player
from world_map import TileMap, WORLD_MAP


# NOTE: consider moving this to another file
class InputHandler:
    def __init__(self, player):
        self.inp = None
        self.player = player

    def get_input(self):
        self.inp = input("What would you like to do?\n> ").lower()

    def perform_action(self, w_map):
        # NOTE: Can change the keyword checking after change with a list from an Action object.
        match self.inp:
            case ('north' | 'south' | 'east' | 'west') as direction:
                # Get adjacent tiles
                if direction in player.get_adjacent_tiles(w_map):
                    player.move(direction)
                else:
                    print("Cannot move that way...\n")

            case 'break':
                # Kill player to end the loop.
                print("Breaking loop by killing player. InputHandler function.")
                player.hp = 0


class Game:
    def __init__(self):
        pass

    def run(self, player, w_map):

        i_handler = InputHandler(player)
        while player.is_alive:
            # Print the tile information to the player
            player_location = w_map.locate_object(player)
            print(player_location, player_location.x, player_location.y)

            # Ask for and handle the players input
            i_handler.get_input()
            i_handler.perform_action(w_map)


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
