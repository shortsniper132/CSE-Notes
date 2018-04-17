command = input  # 1. indent and self.name


class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You picked up the %s." % self.name)


class Armor(Item):
    def __init__(self, name, defense):
        super(Armor, self).__init__(name)
        self.helmet = defense
        self.chest_plate_armor = defense


class Helm(Armor):
    def __init__(self, name, defense):
        super(Helm, self). __init__(name, defense)
        self.chain_helm1 = name
        self.chain_helm2 = defense


class ChainHelm(Helm):
    def __init__(self, name, defense):
        super(ChainHelm, self). __init__(name, defense)

        def wear(self):
            print("You put on the CHAIN HELM.")

        if command == "put on chain helm":
            print(wear)


chain_helm = ChainHelm("chain helmet", 25)


class ChestPlate(Armor):
    def __init__(self, name, defense):
        super(ChestPlate, self). __init__(name, defense)
        self.chain_armor1 = name
        self.chain_armor2 = defense


class ChainChestPlate(ChestPlate):
    def __init__(self, name, defense):
        super(ChainChestPlate, self). __init__(name, defense)

        def wear(self):
            print("You put on the CHAIN CHEST PLATE.")

        if command == "put on chain chest plate":
            print(wear)


chain_chest_plate = ChainChestPlate("chain chest plate", 35)


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self). __init__(name)
        self.dmg = damage


class Range(Weapon):
    def __init__(self, name, damage):
        super(Range, self). __init__(name, damage)


class WoodBow(Range):
    def __init__(self, name, damage):
        super(WoodBow, self). __init__(name, damage)
        self.dmg = damage

        def attack(self):
            print("You attacked with the WOOD BOW.")

        if command == "shoot with wood bow":
            print(attack)


wood_bow = WoodBow("wood bow", 10)


class IronBow(Range):
    def __init__(self, name, damage):
        super(IronBow, self). __init__(name, damage)
        self.dmg = damage

        def attack(self):
            print("You attacked with the IRON BOW.")

        if command == "shoot with iron bow":
            print(attack)


iron_bow = IronBow("iron bow", 25)


class Melee(Weapon):
    def __init__(self, name, damage):
        super(Melee, self). __init__(name, damage)


class WoodShield(Melee):
    def __init__(self, name, defense, damage):
        super(WoodShield, self). __init__(name, damage)
        self.shield = defense

        if command == "pick up wood shield":
            print("You picked the %s." % name)

        def defense(self):
            print("You used your wooden shield.")

        def damage(self):
            print("You attacked with the shield.")

        if command == "defend with wood shield":
            print(defense)
        if command == "attack with wood shield":
            print(damage)


wood_defend = WoodShield("wooden shield", 30, 5)


class IronShield(Melee):
    def __init__(self, name, defense, damage):
        super(IronShield, self). __init__(name, damage)
        self.shield = defense

        def defense(self):
            print("You used your iron shield.")

        def damage(self):
            print("You attacked with the shield.")

        if command == "defend with iron shield":
            print(defense)
        if command == "attack with iron shield":
            print(damage)


iron_defend = IronShield("iron shield", 55, 10)


class Sword(Melee):
    def __init__(self, name, damage):
        super(Sword, self). __init__(name, damage)
        self.name = name
        self.dmg = damage


class WoodSword(Sword):
    def __init__(self, name, damage):
        super(WoodSword, self). __init__(name, damage)
        self.dmg = damage

        def damage(self):
            print("You attacked with the WOOD SWORD.")

        if command == "attack with wood sword":
            print(damage)


wood_sword = WoodSword("wood sword", 15)


class IronSword(Sword):
    def __init__(self, name, damage):
        super(IronSword, self). __init__(name, damage)
        self.dmg = damage

        def damage(self):
            print("You attacked with the STONE SWORD.")

        if command == "attack with stone sword":
            print(damage)


stone_sword = IronSword("stone sword", 30)


class Tool(Item):
    def __init__(self, name):
        super(Tool, self). __init__(name)
        self.name = name


class LightSource(Tool):
    def __init__(self, name):
        super(LightSource, self). __init__(name)


class Torch(LightSource):
    def __init__(self, name, durability):
        super(Torch, self). __init__(name)
        self.torch_light = durability

        def torch_on(self):
            print("You turned on the torch.")

        def torch_off(self):
            print("You turned off torch.")

        if command == "torch on":
            print(torch_on)

        if command == "torch off":
            print(torch_off)


light_source = Torch("torch", 100)


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self). __init__(name)
        self.name = name


class Food(Consumable):
    def __init__(self, name, health_give):
        super(Food, self).__init__(name)
        self.health = health_give


class Container(Consumable):
    def __init__(self, name, health_give):
        super(Container, self). __init__(name)
        self.health = health_give


class HealthPotion(Container):
    def __init__(self, name, health_give):
        super(HealthPotion, self). __init__(name, health_give)

        def drink(self):
            print("You drank the potion.")

        if command == "drink health potion":
            print(drink)


health_potion = HealthPotion("health potion", 55)


class WaterBottle(Container):
    def __init__(self, name, health_give):
        super(WaterBottle, self). __init__(name, health_give)

        def drink(self):
            print("You drank the water from the bottle.")

        if command == "drink water bottle":
            print(drink)


water_bottle = WaterBottle("water bottle", 10)


class RedApple(Food):
    def __init__(self, name, health_give):
        super(RedApple, self). __init__(name, health_give)
        self.health = health_give

        def eat(self):
            print("You ate the RED APPLE.")

        if command == "eat red apple":
            print(eat)


apple1 = RedApple("red apple", 15)


class GreenApple(Food):
    def __init__(self, name, health_give):
        super(GreenApple, self). __init__(name, health_give)
        self.health = health_give

        def eat(self):
            print("You ate the GREEN APPLE.")

        if command == "eat green apple":
            print(eat)


apple2 = GreenApple("green apple", 30)


class GoldApple(Food):
    def __init__(self, name, health_give):
        super(GoldApple, self). __init__(name, health_give)
        self.health = health_give

        def eat(self):
            print("You ate the GOLD APPLE.")

        if command == "eat gold apple":
            print(eat)


apple3 = GoldApple("gold apple", 55)


# LINE


class Character(object):
    def __init__(self, name, health_status, take_damage, inventory, status_effect):
        self.name = name
        self.health_status = health_status
        self.dmg = take_damage
        self.inventory = inventory
        self.status = status_effect


class PlayerName(Character):
    def __init__(self, name):
        super(PlayerName, self). __init__(name, None, None, None, None)


name = PlayerName("SUBJECT 0")


class Health(Character):
    def __init__(self, health_status):
        super(Health, self). __init__(None, health_status, None, None, None)
        self.health = health_status

    def healthy(self):
        print("You are healthy.")

    def not_healthy(self):
        print("You are not healthy.")


current_health = 100


class TakeDMG(Character):
    def __init__(self, take_damage):
        super(TakeDMG, self). __init__(None, None, take_damage, None, None)
        self.damage = take_damage

    def enemy(self):
        print("The enemy attacked.")


dmg = TakeDMG(10)


class Inventory(Character):
    def __init__(self, inventory):
        super(Inventory, self). __init__(None, None, None, Inventory, None)
        self.inventory = inventory

    inventory = 0
    print("You picked up the item.")
    print(1 + + inventory)

    if inventory == 15:
        print("You cannot pick anymore items.")


while False:  # FIX
    class Status(Character):
        def __init__(self, status_effect):
            super(Status, self). __init__(None, None, None, None, status_effect)
            self.status = status_effect

        def poisoned(self):
            self.poison = False
        poison_dmg = -5
        poison_effect = False

        if poison_effect:
            import time
            time.sleep(10)
            print("You are poisoned...")
            Health = current_health + poison_dmg
            print("Your health is at %d." % Health)


# LINE


class Room(object):
    def __init__(self, name, north, west, east, south, up, down, look):
        self.name = name
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down
        self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


outside = Room("Outside of House", 'room1', 'shelter', 'garden', None, None, None,
               "You're outside of a house; there's a garden to the east and a shelter to the west.  There's a house"
               " to the north.")
garden = Room("Garden", None, None, None, None, None, None,
              "You're in a garden and there's a shovel.")
shelter = Room("Shelter", None, 'inside_shelter', "outside", None, None, None,
               "You're in a shelter, there's a path to the west and a door to the east.")
room1 = Room("Entrance of House", 'room2', None, 'closet', 'outside', None, None,
             "You entered your home and you have a path to the north and a door to the east and south; there"
             " is also a table with items.")
room2 = Room("Room 2", 'hallway1', 'kitchen', None, 'room1', None, None,
             "You're in a room and there's a path the the north, west, and south.")
closet = Room("Closet", None, 'room1', 'secret_room', None, None, None,
              "You're in a closet and it's very crowded.")
secret_room = Room("Secret Room", None, 'closet', None, None, None, None,
                   "You entered a secret room and you see lots of scrap metal.")
kitchen = Room("Kitchen", None, None, 'room2', None, None, None,
               "You entered a kitchen, there is also a table.")
hallway1 = Room("Hallway 1", None, 'bedroom1', 'bedroom2', 'room2', 'house_f2', None,
                "You are in a hallway.  There's a room to the east, west, and stairs.")
bedroom1 = Room("Bedroom 1", None, None, 'hallway1', None, None, None,
                "You entered a room and there's lots of furniture and items.")
bedroom2 = Room("Bedroom 2", None, 'hallway1', None, None, None, None,
                "You entered a room and there's lots of furniture and items.")
inside_shelter = Room("Inside of Shelter", "craft", None, 'shelter', None, None, None,
                      "You entered a room and there is a door to the north and a path to the east.")
craft = Room("Crafting Station", None, None, None, 'inside_shelter', None, None,
             "You are in a room; it seems to be a crafting station.")
house_f2 = Room("House F2", None, None, None, None, 'attic', 'hallway1',
                "You entered in a room and there's a ladder, there's a way down the stairs to the south.")
attic = Room("Attic 1", 'attic2', None, None, None, None, "house_f2",
             "You appeared in an attic; nothing is near you.")
attic2 = Room("Attic 2", 'front_house', None, None, 'attic', None, None,
              "You are in an attic with a window to the window.")
front_house = Room("Front of House", "road", None, None, None, None, None,
                   "You appeared on the front side of your house with a road to the north.")
road = Room("Endless Road", None, None, None, None, None, None, "You walked endlessly, but you did not"
                                                                " survive.")  # END GAME
current_node = outside
DIRECTIONS = ["north", "east", "south", "west", "up", "down"]
short_directions = ["n", "e", "s", "w", "u", "d"]

while True:
    print(current_node.name)
    print()
    command = input("CHAT: >_").lower().strip()
    print("")
    if command == "look":
        print(current_node.look)
    print(" ")
    if command == "quit":
        quit(0)

    if command == "pick up":  # FIX
        item = input("Pick up what?  CHAT:>_")
        print()

        if item == "torch":
            print("You picked up the torch.")
            print()

        if item == "green apple":
            print("You picked up the green apple.")
            print()

        if item == "gold apple":
            print("You picked up the gold apple.")
            print()

        if item == "red apple":
            print("You picked up the red apple.")
            print()

        if item == "apple":
            input("What kind of apple?  CHAT:>_")
            print()

            if item == "green apple":
                print("You picked up the green apple.")
                print()

            if item == "gold apple":
                print("You picked up the gold apple.")
                print()

            if item == "red apple":
                print("You picked up the red apple.")
                print()

        if item == "water bottle":
            print("You picked up the water bottle.")
            print()

        if item == "health potion":
            print("You picked up the health potion.")
            print()

        if item == "iron sword":
            print("You picked up the iron sword.")
            print()

        if item == "wood sword":
            print("You picked up the wood sword.")
            print()

        if item == "iron shield":
            print("You picked up the iron shield.")
            print()

        if item == "wood shield":
            print("You picked up the wood shield.")
            print()

        if item == "wood bow":
            print("You picked up the wood bow.")
            print()

        if item == "iron bow":
            print("You picked up the iron bow.")
            print()

        if item == "chest plate":
            input("Pick up what kind of chest plate?  CHAT:>_")
            if item == "chain chest plate":
                print("You picked up the chain chest plate.")
                print()

        if item == "helm":
            input("Pick up what kind of helm?  CHAT:>_")
            print()
            if item == "chain helm":
                print("You picked up the chain helm.")
                print()

    elif command in short_directions:
        position = short_directions.index(command)
        command = DIRECTIONS[position]
    if command in DIRECTIONS:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
            print()
