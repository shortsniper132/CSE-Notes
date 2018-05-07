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
                       "the portal if you do not need the tutorial.", "battle1", None, None, None)

battle1 = Room("Battle Mode", None, None, None, None, None, "combat_training",
               "You entered a battle mode!  Type (evade) to avoid the attack.  You can attack by typing (sword). "
               " Take this wooden sword!  Type (down), or (d), to escape the battle.  There is a LVL 0  enemy.  "
               "< SAND SLIME >", None, "evade", "attack", None)

ruin1 = Room("RUIN-1", "ruin2", None, None, None, None, None,
             "Welcome to RUIN-1, this is where you can type (shop) to open the shop.  There's a room to the "
             "north.", None, None, None, "shop")

ruin2 = Room("RUIN-2", "ruin3", None, None, None, None, None,
             "You entered RUIN-2, there's a path to the north and south.  There is an enemy."
             , "battle2", None, None, None)

battle2 = Room("Battle Mode", None, None, None, None, None, "ruin2",
               "You entered battle mode!  There is a LVL 1 enemy.  < UNDEAD MUMMY >", None, "evade", "attack", None)

ruin3 = Room("RUIN-3", "ruin4", None, None, None, None, None,
             "You entered RUIN-2, there's a path to the north and south.  There is an enemy."
             , "battle3", None, None, None)

battle3 = Room("Battle Mode", None, None, None, None, None, "ruin3",
               "You entered battle mode!  There is a LVL 2 enemy.  < SKELETON >", None, "evade", "attack", None)

ruin4 = Room("RUIN-4", "ruin5", None, None, None, None, None,
             "You entered RUIN-4, there's a path to the north and south.  There is an enemy."
             , "battle4", None, None, None)

battle4 = Room("Battle Mode", None, None, None, None, None, "ruin4",
               "You entered battle mode!  There is a LVL 2 enemy.  < SKELETON >", None, "evade", "attack", None)

ruin5 = Room("RUIN-5", None, None, "ruin6", "ruin4", None, None,
             "You entered RUIN-5, there's a path to the east and south.  There is an enemy."
             , "battle5", None, None, None)

battle5 = Room("Battle Mode", None, None, None, None, None, "ruin5",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None)

ruin6 = Room("RUIN-6", None, "ruin5", "ruin7", None, None, None,
             "You entered RUIN-6, there's a path to the west and east.  There is an enemy."
             , "battle6", None, None, None)

battle6 = Room("Battle Mode", None, None, None, None, None, "ruin6",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None)

ruin7 = Room("RUIN-7", None, "ruin6", "ruin8", None, None, None,
             "You entered RUIN-7, there's a path to the west and east.  There is an enemy."
             , "battle7", None, None, None)

battle7 = Room("Battle Mode", None, None, None, None, None, "ruin7",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None)

ruin8 = Room("RUIN-8", None, "ruin7", "ruin9", None, None, None,
             "You entered RUIN-8, there's a path to the west and east.  There is an enemy."
             , "battle8", None, None, None)

battle8 = Room("Battle Mode", None, None, None, None, None, "ruin8",
               "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None)

ruin9 = Room("RUIN-9", None, "ruin8", None, "ruin10", None, None,
             "You entered RUIN-9, there's a path to the west and south.  There is an enemy."
             , "battle9", None, None, None)

battle9 = Room("Battle Mode", None, None, None, None, None, "ruin9",
               "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None)

ruin10 = Room("RUIN-10", "ruin9", None, None, "ruin11", None, None,
              "You entered RUIN-10, there's a path to the north and south.  There is an enemy."
              , "battle10", None, None, None)

battle10 = Room("Battle Mode", None, None, None, None, None, "ruin10",
                "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None)

ruin11 = Room("RUIN-11", "ruin10", None, None, "ruin12", None, None,
              "You entered RUIN-11, there's a path to the north and south.  There is an enemy."
              , "battle11", None, None, None)

battle11 = Room("Battle Mode", None, None, None, None, None, "ruin11",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None)

ruin12 = Room("RUIN-12", "ruin11", None, None, "ruin13", None, None,
              "You entered RUIN-12, there's a path to the north and south.  There is an enemy."
              , "battle12", None, None, None)

battle12 = Room("Battle Mode", None, None, None, None, None, "ruin12",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None)

ruin13 = Room("RUIN-13", "ruin12", "ruin14", None, None, None, None,
              "You entered RUIN-13, there's a path to the north and west.  There is an enemy."
              , "battle13", None, None, None)

battle13 = Room("Battle Mode", None, None, None, None, None, "ruin13",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None)

ruin14 = Room("RUIN-14", None, "ruin15", "ruin13", None, None, None,
              "You entered RUIN-14, there's a path to the west and east.  There is an enemy."
              , "battle14", None, None, None)

battle14 = Room("Battle Mode", None, None, None, None, None, "ruin14",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None)

ruin15 = Room("RUIN-15", None, "ruin16", "ruin14", None, None, None,
              "You entered RUIN-15, there's a path to the west and east.  There is an enemy."
              , "battle15", None, None, None)

battle15 = Room("Battle Mode", None, None, None, None, None, "ruin15",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None)

ruin16 = Room("RUIN-16", "ruin17", None, "ruin15", None, None, None,
              "You entered RUIN-16, there's a path to the north and east.  There is an enemy."
              , "battle16", None, None, None)

battle16 = Room("Battle Mode", None, None, None, None, None, "ruin16",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None)

ruin17 = Room("RUIN-17", "ruin18", None, None, "ruin16", None, None,
              "You entered RUIN-17, there's a path to the north and south.  There is an enemy."
              , "battle16", None, None, None)

battle17 = Room("Battle Mode", None, None, None, None, None, "ruin17",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None)

ruin18 = Room("RUIN-118", "ruin19", None, None, "ruin17", None, None,
              "You entered RUIN-18, there's a path to the north and south.  There is an enemy."
              , "battle18", None, None, None)

battle18 = Room("Battle Mode", None, None, None, None, None, "ruin18",
                "You entered battle mode!  There is a LVL 7 enemy.  < GOATMAN >", None, "evade", "attack", None)

ruin19 = Room("RUIN-19", None, None, "ruin20", "ruin18", None, None,
              "You entered RUIN-19, there's a path to the east and south.  There is an enemy."
              , "battle19", None, None, None)

battle19 = Room("Battle Mode", None, None, None, None, None, "ruin19",
                "You entered battle mode!  There is a LVL 7 enemy.  < GOATMAN >", None, "evade", "attack", None)

ruin20 = Room("RUIN-20", None, "ruin17", "ruin21", None, None, None,
              "You entered RUIN-20, there's a path to the west and east.  There is an enemy."
              , "battle20", None, None, None)

battle20 = Room("Battle Mode", None, None, None, None, None, "ruin20",
                "You entered battle mode!  There is a LVL 8 enemy.  < UNDEADGOLEM >", None, "evade", "attack", None)

ruin21 = Room("RUIN-21", None, "ruin20", None, "ruin22", None, None,
              "You entered RUIN-21, there's a path to the west and south.  There is an enemy."
              , "battle21", None, None, None)

battle21 = Room("Battle Mode", None, None, None, None, None, "ruin21",
                "You entered battle mode!  There is a LVL 8 enemy.  < UNDEADGOLEM >", None, "evade", "attack", None)

ruin22 = Room("RUIN-22", "ruin21", None, None, "ruin23", None, None,
              "You entered RUIN-22, there's a path to the north and south.  There is an enemy."
              , "battle22", None, None, None)

battle22 = Room("Battle Mode", None, None, None, None, None, "ruin22",
                "You entered battle mode!  There is a LVL 9 enemy.  < SHADOWDEMON >", None, "evade", "attack", None)

ruin23 = Room("RUIN-23", "ruin22", "ruin24", None, None, None, None,
              "You entered RUIN-23, there's a path to the north and west.  There is an enemy."
              , "battle23", None, None, None)

battle23 = Room("Battle Mode", None, None, None, None, None, "ruin23",
                "You entered battle mode!  There is a LVL 9 enemy.  < SHADOWDEMON >", None, "evade", "attack", None)

ruin24 = Room("RUIN-24", "escape", None, "ruin23", None, None, None,
              "You entered RUIN-24, there's a path to the north and east.  You see the corpse of the WRAITH near you."
              , None, None, None, None)

battle24 = Room("Battle Mode", None, None, None, None, None, None,
                "You entered battle mode!  The boss has closed the entrance you came from, you will not be able to "
                "escape.  There is a LVL 10 enemy.  < WRAITH >", None, "evade", "attack", None)

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

    if ruin17 == current_node:
        print("You hear a loud scream up ahead...")
        print()

    if battle1 == current_node:
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
