class Item(object):
    def __init__(self, armor, weapon, consumable, tool):
        self.armor = armor
        self.weapon = weapon
        self.consumable = consumable
        self.tool = tool


class Armor(object):
    def __init__(self, defense):
        self.helmet = defense
        self.chest_plate_armor = defense


class Helm(Armor):
    def __init__(self, defense):
        super(Helm, self). __init__(defense)
        self.chain_helm = defense


class ChainHelm(Helm):
    def __init__(self, defense):
        super(ChainHelm, self). __init__(defense)


chain_helm = ChainHelm(20)


class ChestPlate(Armor):
    def __init__(self, defense):
        super(ChestPlate, self). __init__(defense)
        self.chain_armor = defense


class ChainChestPlate(ChestPlate):
    def __init__(self, defense):
        super(ChainChestPlate, self). __init__(defense)

    def wear(self):
        print("You put on the CHAIN HELM.")


chain_helmet = ChainHelm(30)


class Weapon(object):
    def __init__(self, range_weapon, melee):
        self.ranged_weapon = range_weapon
        self.melee_weapon = melee


class Range(object):
    def __init__(self, name, attack):
        self.name = name
        self.dmg = attack


class WoodBow(Range):
    def __init__(self, name, attack):
        super(WoodBow, self). __init__(WoodBow, attack)
        self.name = name
        self.dmg = attack

    def attack(self):
        print("You attacked with the WOOD BOW.")


wood_bow = WoodBow("WoodBow", 10)


class IronBow(Range):
    def __init__(self, name, attack):
        super(IronBow, self). __init__(IronBow, attack)
        self.name = name
        self.dmg = attack

    def attack(self):
        print("You attacked with the IRON BOW.")


iron_bow = IronBow("IronBow", 25)


class Melee(Weapon):
    def __init__(self, sword):
        super(Melee, self). __init__(Range, Melee)
        self.sword = sword


class Sword(object):
    def __init__(self, name, attack):
        self.name = name
        self.dmg = attack


class WoodSword(Sword):
    def __init__(self, name, attack):
        super(WoodSword, self). __init__(WoodSword, attack)
        self.name = name
        self.dmg = attack

    def attack(self):
        print("You attacked with the WOOD SWORD.")


wood_sword = WoodSword("Wood Sword", 15)


class StoneSword(Sword):
    def __init__(self, name, attack):
        super(StoneSword, self). __init__(StoneSword, attack)
        self.name = name
        self.dmg = attack

    def attack(self):
        print("You attacked with the STONE SWORD.")


stone_sword = StoneSword("Stone Sword", 30)


class Tool(object):
    def __init__(self, torch, hammer):
        self.torch = torch
        self.hammer = hammer


class Torch(Tool):
    def torch(self):
        self.torch()

    def turn_on(self):
        print("You turned on the torch.")

    def turn_off(self):
        print("You turned off the torch.")


class Hammer(object):
    def __init__(self, building_hammer):
        self.hammer = building_hammer


class BuildingHammer(Tool):
    def building_hammer(self):
        self.building_hammer()

    def smash(self):
        print("You smashed the wall.")


class Consumable(object):
    def __init__(self, food, container):
        self.eat = food
        self.drink = container


class Food(Consumable):
    def __init__(self, bread, apple):
        super(Food, self).__init__(bread, apple)
        self.bread = bread
        self.apple = apple


class Container(Consumable):
    def __init__(self, health_potion, water_bottle):
        super(Container, self). __init__(health_potion, water_bottle)
        self.drinkable_health = health_potion
        self.drinkable_water = water_bottle


class HealthPotion(Container):
    def health_potion(self):
        self.health_potion()

    def drink(self):
        print("You drank the potion.")


class WaterBottle(Container):
    def water_bottle(self):
        self.water_bottle()

    def drink(self):
        print("You drank the water from the bottle.")


class Apple(Food):
    def __init__(self, normal_apple, green_apple, gold_apple):
        super(Apple, self). __init__(False, "apple")
        self.apple1 = normal_apple
        self.apple2 = green_apple
        self.apple3 = gold_apple


class GreenApple(Apple):
    def green_apple(self):
        self.green_apple()

    def eat(self):
        print("You eat the GREEN APPLE.")


class GoldApple(Apple):
    def gold_apple(self):
        self.gold_apple()

    def eat(self):
        print("You eat the GOLD APPLE.")


class NormalApple(Apple):
    def normal_apple(self):
        self.normal_apple()

    def eat(self):
        print("You eat the NORMAL APPLE.")
