from tile import Tile

WORLD_MAP = [
    ['x', 'x', 'x'],
    ['x', 'p', 'x'],
    ['x', 'x', 'x'],
]


class TileMap:
    def __init__(self):
        self.tile_map = []

    @property
    def player_start(self):
        for tile in self.tile_map:
            if tile.desc == 'p':
                return tile

    def generate_map(self, prelim_map: list) -> None:
        for row_index, row in enumerate(prelim_map):
            for col_index, col in enumerate(row):
                self.tile_map.append(
                    Tile(row_index, col_index, prelim_map[row_index][col_index]))

    def locate_object(self, object) -> Tile:
        """Returns the tile that a given object is on"""
        for tile in self.tile_map:
            if object.x == tile.x and object.y == tile.y:
                return tile
        # If object isn't found, just return None
        return None
