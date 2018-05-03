command = input


print("Type (help) to look at the guide.")
print()


class Room(object):
    def __init__(self, name, north, west, east, south, up, down, look, battle_mode, evade, attack, shop):
        self.name = name
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down
        self.look = look
        self.evade = evade
        self.attack = attack
        self.shop = shop
        self.battle = battle_mode

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You picked up the %s." % self.name)


class Weapon(Item):
    def __init__(self, name, damage, cost):
        super(Weapon, self). __init__(name)
        self.dmg = damage
        self.cost = cost


class WoodenSword(Weapon):
    def __init__(self, name, damage, cost):
        super(WoodenSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


wooden_sword = WoodenSword("wooden sword", 5, None)


class StoneSword(Weapon):
    def __init__(self, name, damage, cost):
        super(StoneSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


stone_sword = StoneSword("stone sword", 15, 25)


class IronSword(Weapon):
    def __init__(self, name, damage, cost):
        super(IronSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


iron_sword = IronSword("iron sword", 25, 50)


class BoneSword(Weapon):
    def __init__(self, name, damage, cost):
        super(BoneSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


bone_sword = BoneSword("bone sword", 40, 75)


class AxeOfFlame(Weapon):
    def __init__(self, name, damage, cost):
        super(AxeOfFlame, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


axe_of_flame = AxeOfFlame("axe of flame", 55, 100)


class ChillingSpear(Weapon):
    def __init__(self, name, damage, cost):
        super(ChillingSpear, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


chilling_spear = ChillingSpear("chilling spear", 65, 175)


class LegendarySword(Weapon):
    def __init__(self, name, damage, cost):
        super(LegendarySword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


legendary_sword = LegendarySword("iron sword", 80, 300)


class Lurker(Weapon):
    def __init__(self, name, damage, cost):
        super(Lurker, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


lurker = Lurker("lurker", 100, 400)


class FreezingRapier(Weapon):
    def __init__(self, name, damage, cost):
        super(FreezingRapier, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


freezing_rapier = FreezingRapier("freezing rapier", 135, 480)


class GreatAxe(Weapon):
    def __init__(self, name, damage, cost):
        super(GreatAxe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


great_axe = GreatAxe("great axe", 150, 530)


class Blazer(Weapon):
    def __init__(self, name, damage, cost):
        super(Blazer, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


blazer = Blazer("blazer", 180, 690)


class BigFlame(Weapon):
    def __init__(self, name, damage, cost):
        super(BigFlame, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


big_flame = BigFlame("big flame", 230, 690)


class LegendaryAxe(Weapon):
    def __init__(self, name, damage, cost):
        super(LegendaryAxe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


legendary_axe = LegendaryAxe("legendary axe", 270, 800)


class InfinityScythe(Weapon):
    def __init__(self, name, damage, cost):
        super(InfinityScythe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


infinity_scythe = InfinityScythe("infinity scythe", 350, 1000)


class ShadowBlade(Weapon):
    def __init__(self, name, damage, cost):
        super(ShadowBlade, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


shadow_blade = ShadowBlade("shadow blade", 500, 2000)


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self). __init__(name)
        self.name = name


class Container(Consumable):
    def __init__(self, name, health_give, cost):
        super(Container, self). __init__(name)
        self.health = health_give
        self.cost = cost


class HealthP(Container):
    def __init__(self, name, health_give, cost):
        super(HealthP, self). __init__(name, health_give, cost)


health_p = HealthP("health potion", 15, 15)


class SuperHealthP(Container):
    def __init__(self, name, health_give, cost):
        super(SuperHealthP, self). __init__(name, health_give, cost)


super_health_p = SuperHealthP("super health potion", 50, 50)


class Food(Consumable):
    def __init__(self, name, health_give, cost):
        super(Food, self).__init__(name)
        self.health = health_give
        self.cost = cost


class Bread(Food):
    def __init__(self, name, health_give, cost):
        super(Bread, self). __init__(name, health_give, cost)
        self.health = health_give


bread = Bread("bread", 7, 7)


class Apple(Food):
    def __init__(self, name, health_give, cost):
        super(Apple, self). __init__(name, health_give, cost)
        self.health = health_give


apple = Apple("apple", 5, 5)


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
        if command == "test":
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
            poison_dmg = -5
            poison_effect = False

            if poison_effect:
                import time
                time.sleep(10)
                print("You are poisoned...")
                Health = current_health + poison_dmg
                print("Your health is at %d." % Health)

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class ItemBuild(object):
    def __init__(self, name, defense, damage, health_give):
        self.name = name
        self.defense = defense
        self.damage = damage
        self.health_give = health_give


shop_item = [StoneSword, IronSword, BoneSword, AxeOfFlame, ChillingSpear, LegendarySword, Lurker, FreezingRapier,
             GreatAxe, Blazer, BigFlame, LegendaryAxe, InfinityScythe, ShadowBlade, Apple, Bread, HealthP, SuperHealthP]

guide = Room("Guide Room", 'combat_training', None, None, None, None, None,
             "Hello and welcome to RUIN.  In this game, you'll be working your way to find the exit.  Go ahead and "
             "type in (north) or (n) to move onto the next place.", None, None, None, None)

combat_training = Room("Combat Training", None, None, None, None, None, "ruin1",
                       "In this area, you are going to experience a battle.  Simply type (battle), or go "
                       "ahead and press (down), or (d), to go in "
                       "the portal if you do not need the tutorial.", "battle0", None, None, None)

battle0 = Room("Battle Mode", None, None, None, None, None, "combat_training",
               "You entered a battle mode!  Type (evade) to avoid the attack.  You can attack by typing (sword). "
               " Take this wooden sword!  Type (down), or (d), to escape the battle.  There is a LVL 0  enemy.  "
               "< SAND SLIME >", None, "evade", "attack", None)

ruin1 = Room("RUIN-1", "ruin2", None, None, None, None, None,
             "Welcome to RUIN-1, this is where you can type (shop) to open the shop.  There's a room to the "
             "north.", None, None, None, "shop")

ruin2 = Room("RUIN-2", "ruin3", None, None, None, None, None,
             "You entered RUIN-2, there's a path to the north and south.  There are also enemies."
             , "battle1", None, None, None)

battle1 = Room("Battle Mode", None, None, None, None, None, "ruin2",
               "You entered battle mode!  There is a LVL 1 enemy.  < UNDEAD MUMMY >", None, "evade", "attack", None)

ruin3 = Room("RUIN-2", "ruin3", None, None, None, None, None,
             "You entered RUIN-2, there's a path to the north and south.  There are also enemies."
             , "battle1", None, None, None)

battle2 = Room("Battle Mode", None, None, None, None, None, "ruin3",
               "You entered battle mode!  There is a LVL 2 enemy.  < SKELETON >", None, "evade", "attack", None)

ruin3 = Room("RUIN-2", "ruin3", None, None, None, None, None,
             "You entered RUIN-2, there's a path to the north and south.  There are also enemies."
             , "battle1", None, None, None)

battle1 = Room("Battle Mode", None, None, None, None, None, "ruin2",
               "You entered battle mode!  There is a LVL 1 enemy.  < UNDEAD MUMMY >", None, "evade", "attack", None)

shop = Room("Forgotten Shop", None, None, None, None, None, "ruin1",
            "Welcome to the shop.  You will have to battle enemies to get enough money "
            "to buy an item.  Type (down), or (d), to exit the shop.  To buy an item, simply type"
            " (buy).", None, None, None, "shop")

current_node = guide
DIRECTIONS = ["north", "east", "south", "west", "up", "down", "battle", "shop"]
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
        quit(0)  # ADD THIS CODE TO NOT REPEAT!!!
    if command == "help":
        print("Use (n), (w), (e), (s) to move around as for short directions.  Use (north), (west), (east), and (south)"
              " for directions.  Type (look) to look for the description of a room.")
        print()
        print("You can battle an enemy by typing (battle).")
        print()
        print("To get an item, simply type (shop) in RUIN-1.")
        print()
    if battle0 == current_node:
        if command == "evade":
            print("You avoided the enemy's attack.")
            print()
        if command == "attack":
            print("You attacked the enemy.")
            print()

    if shop == current_node:
        if command == "shop":
            print("You have (money.name).")
            print(shop_item)
            print()

    elif command in short_directions:
        position = short_directions.index(command)
        command = DIRECTIONS[position]
    if command in DIRECTIONS:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot do this.")
            print()
