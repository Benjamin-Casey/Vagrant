from tile import Tile
import json

WORLD_MAP = [
    ['f', 'c', 'f'],
    ['f', 'p', 'c'],
    ['c', 'f', 'f'],
]

map_info = json.load(open(file="./tile_info.json", encoding='utf-8'))


class TileMap:
    def __init__(self):
        self.tile_map = []

    @property
    def player_start(self):
        for tile in self.tile_map:
            if tile.name == 'Starting Tile':
                return tile

    def generate_map(self, prelim_map: list) -> None:
        for row_index, row in enumerate(prelim_map):
            for col_index, col in enumerate(row):
                prelim_map_keyword = prelim_map[row_index][col_index]
                tile_info = map_info[prelim_map_keyword]
                self.tile_map.append(
                    Tile(row_index, col_index, tile_info['description'], tile_info['name'], tile_info['items']))

    def locate_object(self, object) -> Tile:
        """Returns the tile that a given object is on"""
        for tile in self.tile_map:
            if object.x == tile.x and object.y == tile.y:
                return tile
        # If object isn't found, just return None
        return None

    def adjacent_tiles(self, object) -> list:
        adj_tiles = {}

        for tile in self.tile_map:
            if object.x == tile.x and object.y == tile.y + 1:
                adj_tiles['south'] = tile
            if object.x == tile.x and object.y == tile.y - 1:
                adj_tiles['north'] = tile
            if object.y == tile.y and object.x == tile.x + 1:
                adj_tiles['west'] = tile
            if object.y == tile.y and object.x == tile.x - 1:
                adj_tiles['east'] = tile

        return adj_tiles
