class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 100
        self.inventory = []

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def take_item(self, item, tile) -> None:
        if item in tile.items:
            self.inventory.append(item.capitalize())
            tile.items.remove(item)
        else:
            print("Could not find that item!")

    def adjust_hp(self, amt: int) -> int:
        self.hp += amt
        return self.hp

    def print_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(item)
        else:
            print("No items in inventory!")

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
        self.x = x
        self.y = y
        return (self.x, self.y)
