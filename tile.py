from items import Item

# TODO consider adding conditional description as well as the condition.

class Tile:
    def __init__(self, x, y, desc, *items):
        self.x = x
        self.y = y
        self.desc = desc
        self.items = items

    def __str__(self):
        return self.desc      

tiles = [Tile(0, 0, "Tile 0, 0"), Tile(0, 1, "Tile 0, 1"), 
         Tile(1, 0, "Tile 1, 0"), Tile(1, 1, "Tile 1,1,")]