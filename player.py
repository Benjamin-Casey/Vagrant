from action import Action


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 100
        self.inventory = []

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def adjust_hp(self, amt: int) -> int:
        self.hp += amt
        return self.hp

    def print_inventory(self):
        for item in self.inventory:
            print(item)

    def move(self, direction: str) -> None:
        match direction.lower():
            case 'north':
                self.y += 1
            case 'south':
                self.y -= 1
            case 'east':
                self.x += 1
            case 'west':
                self.x -= 1

    def set_location(self, x: int, y: int) -> tuple:
        self.x == x
        self.y == y
        return (self.x, self.y)

    def get_adjacent_tiles(self, world: list) -> list:
        adjacent_tiles = {}
        for tile in world.tile_map:
            if tile.x == self.x and tile.y == self.y + 1:
                adjacent_tiles['north'] = tile
                # self.available_actions.append(
                    # Action("Move North", self.move_north, ["north", "n"]))
            elif tile.x == self.x and tile.y == self.y - 1:
                adjacent_tiles['south'] = tile
                # self.available_actions.append(
                    # Action("Move South", self.move_south, ["south", "s"]))
            elif tile.y == self.y and tile.x == self.x + 1:
                adjacent_tiles['east'] = tile
                # self.available_actions.append(
                    # Action("Move East", self.move_east, ["east", "e"]))
            elif tile.y == self.y and tile.x == self.x - 1:
                adjacent_tiles['west'] = tile
                # self.available_actions.append(
                    # Action("Move West", self.move_west, ["west", "w"]))
        return adjacent_tiles