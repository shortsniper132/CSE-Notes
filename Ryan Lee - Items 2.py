class Item(object):
    def __init__(self, armor, weapon, consumable, tool):
        self.armor = armor
        self.weapon = weapon
        self.consumable = consumable
        self.tool = tool

    def pick_up(self):
        print("You picked up the item.")


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

    def wear(self):
        print("You put on the CHAIN HELM.")


chain_helm = ChainHelm(20)


class ChestPlate(Armor):
    def __init__(self, defense):
        super(ChestPlate, self). __init__(defense)
        self.chain_armor = defense


class ChainChestPlate(ChestPlate):
    def __init__(self, defense):
        super(ChainChestPlate, self). __init__(defense)

    def wear(self):
        print("You put on the CHAIN CHEST PLATE.")


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
    def __init__(self, sword, shield):
        super(Melee, self). __init__(Range, Melee)
        self.sword = sword
        self.shield = shield


class WoodShield(object):
    def __init__(self,name, defend_self):
        self.name = name
        self.shield = defend_self

    def defend(self):
        print("You pulled out your wooden shield.")


wood_defend = WoodShield("Wooden Shield", 30)


class IronShield(object):
    def __init__(self, name, defend_self):
        self.name = name
        self.shield = defend_self

    def defend(self):
        print("You pulled out your iron shield.")


iron_defend = IronShield("Iron Shield", 55)


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
    def __init(self, light):
        self.torch = light

    def turn_on(self):
        print("You turned on the torch.")

    def turn_off(self):
        print("You turned off the torch.")


class Hammer(object):
    def __init__(self, building_hammer):
        self.hammer = building_hammer


class BuildingHammer(Hammer):
    def __init__(self, build):
        super(BuildingHammer, self). __init__(build)
        self.building_hammer = build

    def build(self):
        print("You built an item.")


class Consumable(object):
    def __init__(self, food, container):
        self.eat = food
        self.drink = container


class Food(Consumable):
    def __init__(self, apple):
        super(Food, self).__init__(apple, False)
        self.apple = apple


class Container(Consumable):
    def __init__(self, drinkable):
        super(Container, self). __init__(False, drinkable)
        self.drinkable_drink = drinkable


class HealthPotion(object):
    def __init__(self, drink, health_amount):
        self.health_potion = drink
        self.health = health_amount

    def drink(self):
        print("You drank the potion.")

    def health(self):
        health_amount = 45


class WaterBottle(object):
    def __init__(self, drink, health_amount):
        self.water_bottle = drink
        self.health = health_amount

    def drink(self):
        print("You drank the water from the bottle.")

    def health(self):
        health_amount = 15


class Apple(Food):
    def __init__(self, apple, green_apple, gold_apple, normal_apple):
        super(Apple, self). __init__(apple)
        self.apple = green_apple
        self.apple = gold_apple
        self.apple = normal_apple


class GreenApple(object):
    def __init__(self, eat, health_give):
        self.green_apple = eat
        self.health = health_give

    def eat(self):
        print("You eat the GREEN APPLE.")

    def health(self):
        health_amount = 35


class GoldApple(object):
    def __init__(self, eat, health_give):
        self.gold_apple = eat
        self.health = health_give

    def eat(self):
        print("You eat the GOLD APPLE.")

    def health(self):
        health_amount = 55


class NormalApple(object):
    def __init__(self, eat, health_give):
        self.normal_apple = eat
        self.health = health_give

    def eat(self):
        print("You eat the NORMAL APPLE.")

    def health(self):
        health_amount = 20
