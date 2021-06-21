from player import p

class Action:
    def __init__(self, name, function, hotkey):
        self.name = name
        self.function = function
        self.hotkey = hotkey

actions = [Action("Move North", p.move_north, ["north", "n"]),
           Action("Move South", p.move_south, ["south", "s"]),
           Action("Move East", p.move_east, ["east", "e"]),
           Action("Move West", p.move_west, ["west", "w"])]