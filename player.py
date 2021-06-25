from action import Action

# TODO give player self.location = get_location()
# every time player.location is asked, it calls get lcoation
# need to import world from tiles or something and have that
# in the get_tile fucntion instead of 'tiles' as a param
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.inventory = []
        self.available_actions = []

    def get_tile(self, tiles):
        for tile in tiles:
            if tile.x == self.x and tile.y == self.y:
                return tile

    def print_inventory(self):
        for item in self.inventory:
            print(item)

    def take_item(self, item_name, tile):
        for item in tile.items:
            if item.name.lower() == item_name:
                self.inventory.append(item)
                tile.items.remove(item)
                break

    def move_north(self):
        self.y += 1
    def move_south(self):
        self.y -= 1
    def move_east(self):
        self.x += 1
    def move_west(self):
        self.x -= 1

    def get_adjacent_tiles(self, world):
        adj = []
        for tile in world:
            if tile.x == self.x and tile.y == self.y + 1:
                adj.append(tile)
                self.available_actions.append(Action("Move North", self.move_north, ["north", "n"]))
            elif tile.x == self.x and tile.y == self.y - 1:
                adj.append(tile)
                self.available_actions.append(Action("Move South", self.move_south, ["south", "s"]))
            elif tile.y == self.y and tile.x == self.x + 1:
                adj.append(tile)
                self.available_actions.append(Action("Move East", self.move_east, ["east", "e"]))
            elif tile.y == self.y and tile.x == self.x - 1:
                adj.append(tile)
                self.available_actions.append(Action("Move West", self.move_west, ["west", "w"]))
        #return adj

    # TODO possibly put this on the tile rather than as a player method
    def get_actions(self, current_tile):
        # Check if the tile has items
        if current_tile.items:
            self.available_actions.append(Action("Take Item", self.take_item, ["take"]))

p = Player()