class Tile:
    def __init__(self, x, y, desc):
        self.x = x
        self.y = y
        self.desc = desc

    def __repr__(self):
        return self.desc
