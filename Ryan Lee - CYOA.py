command = input


print("Type (help) to look at the guide.")
print()


class Room(object):
    def __init__(self, name, north, west, east, south, up, down, look, battle_mode, evade, attack, shop, enemy):
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
        self.enemy = enemy

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


legendary_sword = LegendarySword("legendary sword", 80, 300)


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


great_axe = GreatAxe("great axe", 170, 560)


class Blazer(Weapon):
    def __init__(self, name, damage, cost):
        super(Blazer, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


blazer = Blazer("blazer", 230, 700)


class BigFlame(Weapon):
    def __init__(self, name, damage, cost):
        super(BigFlame, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


big_flame = BigFlame("big flame", 320, 900)


class LegendaryAxe(Weapon):
    def __init__(self, name, damage, cost):
        super(LegendaryAxe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


legendary_axe = LegendaryAxe("legendary axe", 450, 1500)


class InfinityScythe(Weapon):
    def __init__(self, name, damage, cost):
        super(InfinityScythe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


infinity_scythe = InfinityScythe("infinity scythe", 600, 2000)


class ShadowBlade(Weapon):
    def __init__(self, name, damage, cost):
        super(ShadowBlade, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost


shadow_blade = ShadowBlade("shadow blade", 1000, 3000)


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


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Character(object):
    def __init__(self, character_name, health, inventory, coin, equip):
        self.name = character_name
        self.health = health
        self.inventory = inventory
        self.coin = coin


class Name(Character):
    def __init__(self, character_name):
        super(Name, self). __init__(character_name, None, None, None)
        self.character_name = character_name


class Health(Character):
    def __init__(self, health):
        super(Health, self). __init__(None, health, None, None)
        self.health = health
    health = 100
    if health == 0:
        print("You were killed.")
        quit(0)


class Inventory(Character):
    def __init__(self, inventory):
        super(Inventory, self). __init__(None, None, inventory, None)
        inventory = []

        while True:
            inventory.append(Inventory)


class Coins(Character):
    def __init__(self, coin):
        super(Coins, self). __init__(None, None, None, coin)
    coin = 0


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Enemies(object):
    def __init__(self, name, health, damage, coin_drop):
        self.name = name
        self.health = health
        self.damage = damage
        self.coin_drop = coin_drop


class SandSlime(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(SandSlime, self).__init__(name, health, damage, coin_drop)


ss = SandSlime("Sand Slime", 30, -2, 2)


class UndeadMummy(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(UndeadMummy, self).__init__(name, health, damage, coin_drop)


um = UndeadMummy("Undead Mummy", 60, -5, 3)


class Skeleton(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Skeleton, self).__init__(name, health, damage, coin_drop)


s = Skeleton("Skeleton", 90, -3, 4)


class EyeShot(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(EyeShot, self).__init__(name, health, damage, coin_drop)


es = EyeShot("Eye Shot", 50, -15, 4)


class Carnage(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Carnage, self).__init__(name, health, damage, coin_drop)


c = Carnage("Carnage", 350, -6, 5)


class SuperMummy(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(SuperMummy, self).__init__(name, health, damage, coin_drop)


sm = SuperMummy("Super Mummy", 500, -5, 7)


class Destroyer(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Destroyer, self).__init__(name, health, damage, coin_drop)


d = Destroyer("Destroyer", 750, -3, 9)


class GoatMan(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(GoatMan, self).__init__(name, health, damage, coin_drop)


gm = GoatMan("Goat Man", 1500, -10, 13)


class UndeadGolem(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(UndeadGolem, self).__init__(name, health, damage, coin_drop)


ug = UndeadGolem("Undead Golem", 2000, -15, 25)


class ShadowDemon(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(ShadowDemon, self).__init__(name, health, damage, coin_drop)


sd = ShadowDemon("Shadow Demon", 4000, -5, 35)


class Wraith(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Wraith, self).__init__(name, health, damage, coin_drop)


w = Wraith("Wraith", 8000, -25, 0)


class Anubis(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Anubis, self).__init__(name, health, damage, coin_drop)


a = Anubis("Anubis", 300000, -10, 0)


class END(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(END, self).__init__(name, health, damage, coin_drop)


e = END("END", 5000, -100, 0)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


shop_item = [StoneSword, IronSword, BoneSword, AxeOfFlame, ChillingSpear, LegendarySword, Lurker, FreezingRapier,
             GreatAxe, Blazer, BigFlame, LegendaryAxe, InfinityScythe, ShadowBlade, Apple, Bread, HealthP, SuperHealthP]

shop_itemNAMES = ["Stone Sword", "Iron Sword", "Bone Sword", "Axe Of Flame", "Chilling Spear", "Legendary Sword",
                  "Lurker", "Freezing Rapier", "Great Axe", "Blazer", "Big Flame", "Legendary Axe", "Infinity Scythe",
                  "Shadow Blade", "Apple", "Bread", "Health Potion", "Super Health Potion"]

guide = Room("Guide Room", 'combat_training', None, None, None, None, None,
             "Hello and welcome to RUIN.  In this game, you'll be working your way to find the exit.  Go ahead and "
             "type in (north) or (n) to move onto the next place.", None, None, None, None, None)

combat_training = Room("Combat Training", None, None, None, None, None, "ruin1",
                       "In this area, you are going to experience a battle.  Simply type (battle), or go "
                       "ahead and press (down), or (d), to go in "
                       "the portal if you do not need the tutorial.", "battle1", None, None, None, None)

battle1 = Room("Battle Mode", None, None, None, None, None, "combat_training",
               "You entered a battle mode!  Type (evade) to avoid the attack.  You can attack by typing (sword). "
               " Take this wooden sword!  Type (down), or (d), to escape the battle.  There is a LVL 0  enemy.  "
               "< SAND SLIME >", None, "evade", "attack", None, SandSlime)

ruin1 = Room("RUIN-1", "ruin2", None, None, None, None, None,
             "Welcome to RUIN-1, this is where you can type (shop) to open the shop.  There's a room to the "
             "north.", None, None, None, "shop", None)

ruin2 = Room("RUIN-2", "ruin3", None, None, None, None, None,
             "You entered RUIN-2, there's a path to the north and south.  There is an enemy.",
             "battle2", None, None, None, None)

battle2 = Room("Battle Mode", None, None, None, None, None, "ruin2",
               "You entered battle mode!  There is a LVL 1 enemy.  < UNDEAD MUMMY >", None, "evade", "attack", None,
               UndeadMummy)

ruin3 = Room("RUIN-3", "ruin4", "grave1", None, None, None, None,
             "You entered RUIN-2, there's a path to the north and south.  There is an enemy.",
             "battle3", None, None, None, None)

grave1 = Room("Grave-1", None, None, "ruin3", None, None, None, "You entered a room, there's a grave and a path to the "
              " east.", None, None, None, None, None)

battle3 = Room("Battle Mode", None, None, None, None, None, "ruin3",
               "You entered battle mode!  There is a LVL 2 enemy.  < SKELETON >", None, "evade", "attack", None,
               Skeleton)

ruin4 = Room("RUIN-4", "ruin5", None, None, None, None, None,
             "You entered RUIN-4, there's a path to the north and south.  There is an enemy.",
             "battle4", None, None, None, None)

battle4 = Room("Battle Mode", None, None, None, None, None, "ruin4",
               "You entered battle mode!  There is a LVL 2 enemy.  < SKELETON >", None, "evade", "attack", None,
               Skeleton)

ruin5 = Room("RUIN-5", None, None, "ruin6", "ruin4", None, None,
             "You entered RUIN-5, there's a path to the east and south.  There is an enemy.",
             "battle5", None, None, None, None)

battle5 = Room("Battle Mode", None, None, None, None, None, "ruin5",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None,
               EyeShot)

ruin6 = Room("RUIN-6", None, "ruin5", "ruin7", None, None, None,
             "You entered RUIN-6, there's a path to the west and east.  There is an enemy.",
             "battle6", None, None, None, None)

battle6 = Room("Battle Mode", None, None, None, None, None, "ruin6",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None,
               EyeShot)

ruin7 = Room("RUIN-7", "grave2", "ruin6", "ruin8", None, None, None,
             "You entered RUIN-7, there's a path to the west and east.  There is an enemy.",
             "battle7", None, None, None, None)

grave2 = Room("Grave-2", None, None, None, "ruin7", None, None, "You entered a room, there's a grave and a path to the "
              " south.", None, None, None, None, None)

battle7 = Room("Battle Mode", None, None, None, None, None, "ruin7",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None,
               EyeShot)

ruin8 = Room("RUIN-8", None, "ruin7", "ruin9", None, None, None,
             "You entered RUIN-8, there's a path to the west and east.  There is an enemy.",
             "battle8", None, None, None, None)

battle8 = Room("Battle Mode", None, None, None, None, None, "ruin8",
               "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None, Carnage)

ruin9 = Room("RUIN-9", None, "ruin8", None, "ruin10", None, None,
             "You entered RUIN-9, there's a path to the west and south.  There is an enemy.",
             "battle9", None, None, None, None)

battle9 = Room("Battle Mode", None, None, None, None, None, "ruin9",
               "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None, Carnage)

ruin10 = Room("RUIN-10", "ruin9", None, None, "ruin11", None, None,
              "You entered RUIN-10, there's a path to the north and south.  There is an enemy.",
              "battle10", None, None, None, None)

battle10 = Room("Battle Mode", None, None, None, None, None, "ruin10",
                "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None,
                Carnage)

ruin11 = Room("RUIN-11", "ruin10", None, "grave3", "ruin12", None, None,
              "You entered RUIN-11, there's a path to the north and south.  There is an enemy.",
              "battle11", None, None, None, None)

grave3 = Room("Grave-3", None, "ruin11", None, None, None, None,
              "You entered a room, there's a grave and a path to the "
              " west.", None, None, None, None, None)

battle11 = Room("Battle Mode", None, None, None, None, None, "ruin11",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None,
                SuperMummy)

ruin12 = Room("RUIN-12", "ruin11", None, None, "ruin13", None, None,
              "You entered RUIN-12, there's a path to the north and south.  There is an enemy.",
              "battle12", None, None, None, None)

battle12 = Room("Battle Mode", None, None, None, None, None, "ruin12",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None,
                SuperMummy)

ruin13 = Room("RUIN-13", "ruin12", "ruin14", None, None, None, None,
              "You entered RUIN-13, there's a path to the north and west.  There is an enemy.",
              "battle13", None, None, None, None)

battle13 = Room("Battle Mode", None, None, None, None, None, "ruin13",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None,
                SuperMummy)

ruin14 = Room("RUIN-14", None, "ruin15", "ruin13", None, None, None,
              "You entered RUIN-14, there's a path to the west and east.  There is an enemy.",
              "battle14", None, None, None, None)

battle14 = Room("Battle Mode", None, None, None, None, None, "ruin14",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer)

ruin15 = Room("RUIN-15", None, "ruin16", "ruin14", "grave4", None, None,
              "You entered RUIN-15, there's a path to the west and east.  There is an enemy.",
              "battle15", None, None, None, None)

grave4 = Room("Grave-4", "ruin15", None, None, None, None, None,
              "You entered a room, there's a grave and a path to the "
              " north.", None, None, None, None, None)

battle15 = Room("Battle Mode", None, None, None, None, None, "ruin15",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer)

ruin16 = Room("RUIN-16", "ruin17", None, "ruin15", None, None, None,
              "You entered RUIN-16, there's a path to the north and east.  There is an enemy.",
              "battle16", None, None, None, None)

battle16 = Room("Battle Mode", None, None, None, None, None, "ruin16",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer)

ruin17 = Room("RUIN-17", "ruin18", None, None, "ruin16", None, None,
              "You entered RUIN-17, there's a path to the north and south.  There is an enemy.",
              "battle16", None, None, None, None)

battle17 = Room("Battle Mode", None, None, None, None, None, "ruin17",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer)

ruin18 = Room("RUIN-118", "ruin19", None, None, "ruin17", None, None,
              "You entered RUIN-18, there's a path to the north and south.  There is an enemy.",
              "battle18", None, None, None, None)

battle18 = Room("Battle Mode", None, None, None, None, None, "ruin18",
                "You entered battle mode!  There is a LVL 7 enemy.  < GOAT MAN >", None, "evade", "attack", None,
                GoatMan)

ruin19 = Room("RUIN-19", None, None, "ruin20", "ruin18", None, None,
              "You entered RUIN-19, there's a path to the east and south.  There is an enemy.",
              "battle19", None, None, None, None)

battle19 = Room("Battle Mode", None, None, None, None, None, "ruin19",
                "You entered battle mode!  There is a LVL 7 enemy.  < GOAT MAN >", None, "evade", "attack", None,
                GoatMan)

ruin20 = Room("RUIN-20", None, "ruin17", "ruin21", None, None, None,
              "You entered RUIN-20, there's a path to the west and east.  There is an enemy.",
              "battle20", None, None, None, None)

battle20 = Room("Battle Mode", None, None, None, None, None, "ruin20",
                "You entered battle mode!  There is a LVL 8 enemy.  < UNDEAD GOLEM >", None, "evade", "attack", None,
                UndeadGolem)

ruin21 = Room("RUIN-21", None, "ruin20", None, "ruin22", None, None,
              "You entered RUIN-21, there's a path to the west and south.  There is an enemy.",
              "battle21", None, None, None, None)

battle21 = Room("Battle Mode", None, None, None, None, None, "ruin21",
                "You entered battle mode!  There is a LVL 8 enemy.  < UNDEAD GOLEM >", None, "evade", "attack", None,
                UndeadGolem)

ruin22 = Room("RUIN-22", "ruin21", None, None, "ruin23", None, None,
              "You entered RUIN-22, there's a path to the north and south.  There is an enemy.",
              "battle22", None, None, None, None)

battle22 = Room("Battle Mode", None, None, None, None, None, "ruin22",
                "You entered battle mode!  There is a LVL 9 enemy.  < SHADOW DEMON >", None, "evade", "attack", None,
                ShadowDemon)

ruin23 = Room("RUIN-23", "ruin22", "battle24", None, None, None, None,
              "You entered RUIN-23, there's a path to the north and west.  There is an enemy.",
              "battle23", None, None, None, None)

battle23 = Room("Battle Mode", None, None, None, None, None, "ruin23",
                "You entered battle mode!  There is a LVL 9 enemy.  < SHADOW DEMON >", None, "evade", "attack", None,
                ShadowDemon)

battle24 = Room("Battle Mode", None, None, None, None, None, None,
                "You entered battle mode!  The boss has closed the entrance you came from, you will not be able to "
                "escape...  There is a LVL 10 enemy.  < WRAITH >", None, "evade", "attack", None, Wraith)

ruin24 = Room("RUIN-24", "end", None, "ruin23", None, None, None,
              "You entered RUIN-24, there's a path to the north and east.  You see the corpse of the WRAITH near you.",
              None, None, None, None, None)

end = Room("END", None, None, None, None, "exit0", "endBOSS", "You entered the END, there's a ladder which leads up.",
           None, None, None, None, None)

exit0 = Room("Escaped...", None, None, None, None, None, None, "You exit from the ground.  You walked away from the "
             "place you came from, and you were never seen again, but you became a legend.", None, None, None, None,
             None)

endBOSS = Room("Battle Mode", None, None, None, None, None, "end",
               "You entered battle mode...  There is an enemy.  < END >", None, "evade", "attack", None, END)

shop = Room("Forgotten Shop", None, None, None, None, None, "ruin1",
            "Welcome to the shop.  You will have to battle enemies to get enough money "
            "to buy an item.  Type (down) to exit the shop.  To see the items, simply type (shop).",
            None, None, None, "shop", None)

battleANUBIS = Room("UNDERWORLD", None, None, None, None, None, None,
                    "You entered battle mode!  There is an enemy.  < ANUBIS >", None, "evade", "attack", None, Anubis)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


current_node = guide
DIRECTIONS = ["north", "east", "south", "west", "up", "down", "battle", "shop"]
short_directions = ["n", "e", "s", "w", "u", "d"]

while True:
    print(current_node.name)
    print()
    command = input("CHAT: >_").lower().strip()
    print()
    print("---------------------------------------------------------------------------------------------------")
    print()
    if current_node == combat_training:
        wooden_sword = True
    if command == "look":
        print(current_node.look)
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()
    if command == "quit":
        print("You quit the game...")
        quit(0)
    if command == "help":
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()
        print("GUIDE:")
        print("Use (n), (w), (e), (s) to move around as for short directions.  Use (north), (west), (east), and (south)"
              " for directions.  Type (look) to look for the description of a room.")
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()
        print("You can battle an enemy by typing (battle).")
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()
        print("To get an item, simply type (shop) in RUIN-1.")
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()

    if ruin17 == current_node:
        print("You hear a loud scream up ahead...")
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()

    if endBOSS == current_node:
        print("END:  It seems you've found me... I shouldn't let you win, prepare to taste defeat!")
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()

    if command == "inventory":
        print("This is what you have.")
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()
        print("INVENTORY:")
        print(Inventory)
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()
        input("What do you want to use?  CHAT: >_")
        print()
        print("---------------------------------------------------------------------------------------------------")
        print()

    if grave1 == current_node:
        if command == "hit grave":
            print("ANUBIS:  You shouldn't have done that...  ( ANUBIS ATTACKS! )")
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            current_node = battleANUBIS

    if exit0 == current_node:
        exit(0)

    if battle1 == current_node:
        if command == "evade":
            print("You avoided the enemy's attack.")
            print()
            print("The sand slime attacked!")
            print("It missed!")
            print("Your health is at %d." % Health.health)
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
        if command == "attack":
            print("You attacked the enemy.")
            print("The health of the Sand Slime is 0.")
            print()
            print("The Sand Slime attacked!")
            print("Your health is at %d." % Health.health)
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()

    if shop == current_node:
        if command == "shop":

            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            print("SHOP ITEM:")
            print(shop_itemNAMES)
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            print("You have %d coins." % Coins.coin)
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            if input("SHOP KEEPER:  What do you want to need?  You can type (details) for the details of the items, or "
                     "(buy) to buy an item.   CHAT: >_"):
                print()
                print("-----------------------------------------------------------------------------------------------")
                print()
            choice = ["details", "buy"]
            if command == "details":
                    print("details")

            if command == "buy":
                print("buy")

    elif command in short_directions:
        position = short_directions.index(command)
        command = DIRECTIONS[position]
    if command in DIRECTIONS:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot do this.")
            print()
