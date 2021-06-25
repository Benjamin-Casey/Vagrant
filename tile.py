from items import Item
"""
Tile is the superclass for all tiles in the world.

If a tile has special features or properties, a new subclass for that 
tile will need to be declared so that it's own features can be written 
into it.
"""
class Tile:
    def __init__(self, x, y, desc, *items):
        self.x = x
        self.y = y
        self.desc = desc
        self.items = items

    def __repr__(self):
        return self.desc

    def check_item(self, item):
        return any(i.name == item for i in self.items)
  
# NOTE: See bottom of file for new world.
old_world = [
    Tile(0, 0, "Tile 0, 0"), Tile(0, 1, "Tile 0, 1"), 
    Tile(1, 0, "Tile 1, 0"), Tile(1, 1, "Tile 1, 1")
]


# TODO rewrite this to be a sublcass, then an object of the subclass.
# TODO allow actions to be added to the available actions from tiles.
# E.g: "Enter house" should be a command from North_Field that calls move_north()
class Start_Tile(Tile):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.desc = "You stand in an open field next to an old tree stump."
        self.items = [Item("apple", "A shiny, red apple.")]

    def __repr__(self):
        if self.check_item("apple"): 
            return self.desc + "\nAn apple sits on the stump."
        else:
            return self.desc


class North_Field(Tile):
    def __init__(self):
        self.x = 0
        self.y = 1
        self.desc = "In the Northern part of the field is an old, dilapidated house."
        self.items = [Item("Rock", "Dull and lifeless.")]

    def __repr__(self):
        if self.check_item("Rock"):
            return self.desc + "\nYou notice a fist sized rock in the field. Perhaps you can take it with you."
        else:
            return self.desc


class Dilapidated_House:
    def __init__(self):
        self.x = 0
        self.y = 2
        self.desc = ""


world = [
    Start_Tile(),
    North_Field()
]