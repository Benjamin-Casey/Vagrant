class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.inventory = []

    def get_tile(self, tiles):
        for tile in tiles:
            if tile.x == self.x and tile.y == self.y:
                return tile

    def move_north(self):
        self.y += 1
    def move_south(self):
        self.y -= 1
    def move_east(self):
        self.x += 1
    def move_west(self):
        self.x -= 1

p = Player()