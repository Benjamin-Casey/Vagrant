class Tile:
    def __init__(self, x, y, desc, name, items=[]):
        self.x = x
        self.y = y
        self.desc = desc
        self.name = name
        self.items = items

    def __str__(self):
        output = f"{self.desc}\n"
        for item in self.items:
            output += f"There is a {item.lower()} here.\n"
        return output


# class TileBuilder:
#     def __init__(self, prebuild_tile_map):
#         self.prebuild_tile_map = prebuild_tile_map

#     def build_tiles(self) -> Tile:
#         for tile in self.prebuild_tile_map:
#             """
#             Tile has an x, y, desc and item slot attached to it.

#             What if the tile description stored all the information about keys, tiles, etc. in it as well
#             Then the tile builder can check its hash value or some shit, then generate the relevant tile off of that.

#             Need some sort of file that stores different tile information e.g house, forest, etc.
#             """

#         t_loc = (tile.x, tile.y)
#         t_desc = tile.desc
#         t_items = tile.items

#         return Tile(t_loc[0], t_loc[1], t_desc, t_items)

#     def build_tile(self, prelim_tile: str) -> Tile:
#         pass
