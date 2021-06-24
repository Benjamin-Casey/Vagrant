from items import Item

class Tile:
    def __init__(self, x, y, desc):
        self.x = x
        self.y = y
        self.desc = desc

    def __repr__(self):
        return self.desc    
  

world = [Tile(0, 0, "Tile 0, 0"), Tile(0, 1, "Tile 0, 1"), 
         Tile(1, 0, "Tile 1, 0"), Tile(1, 1, "Tile 1, 1")]


# Apple = Item("Apple", "Shiny red apple")

# class Start_Tile:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.desc = "You stand in an open field next to an old tree stump."
#         self.items = [Apple]

#     def __repr__(self):
#         if Apple in self.items: 
#             return self.desc + "\nAn apple sits on the stump."
#         else:
#             return self.desc

#     # If apple in items:
#     #    available_actions.append(take item)


# s = Start_Tile()
# print(s)