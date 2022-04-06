import json

item_info = json.load(open(file="./items.json", encoding="utf-8"))


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return """{}\n--------\n{}""".format(self.name, self.description, self.items)


class Weapon(Item):
    def __init__(self, name, description, attack):
        self.name = name
        self.description = description
        self.attack = attack

class ItemBuilder:
    def build_item(self, item_list : list) -> list:
        # Check that the list isn't empty
        if len(item_list) > 0:
            # Cross-reference the item with item_data from items.json
            for item in item_list:
                if item.lower() in item_info.keys():    # Check that the item name is in item_info
                    if item_info[item.lower()]