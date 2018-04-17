class Item(object):
    def __init__(self, armor, weapon, consumable, tool):
        self.armor = armor
        self.weapon = weapon
        self.consumable = consumable
        self.tool = tool


class Armor(object):
    def __init__(self, helm, chest_plate):
        self.helmet = helm
        self.chest_plate_armor = chest_plate


class Helm(object):
    def __init__(self, chain_helmet, super_helmet):
        self.chain_helm = chain_helmet
        self.super_helm = super_helmet


class ChestPlate(object):
    def __init__(self, chain_chest_plate, super_chest_plate):
        self.chain_armor = chain_chest_plate
        self.super_armor = super_chest_plate


class Weapon(object):
    def __init__(self, range_weapon, melee):
        self.ranged_weapon = range_weapon
        self.melee_weapon = melee


class Tool(object):
    def __init__(self, torch, hammer):
        self.torch = torch
        self.hammer = hammer


class Consumable(object):
    def __init__(self, food, container):
        self.eat = food
        self.drink = container


class Food(object):
    def __init__(self, bread, apple):
        self.bread = bread
        self.apple = apple


class Container(object):
    def __init__(self, health_potion, water_bottle):
        self.drinkable_health = health_potion
        self.drinkable_water = water_bottle


class Apple(object):
    def __init__(self, normal_apple, green_apple, gold_apple):
        self.apple1 = normal_apple
        self.apple2 = green_apple
        self.apple3 = gold_apple


class Torch(Tool):
    def tool(self):
        if command


class Consumable(object):
    def __init__(self, food, container):
        self.eat = food
        self.drink = container


class Consumable(object):
    def __init__(self, food, container):
        self.eat = food
        self.drink = container
