from action import Action

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

    def take_item(self, item, tile):
        self.inventory += item
        tile.items -= item

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


p = Player()