import random
command = input
print()
print("GUIDE:")
print()
print("Use (n), (w), (e), (s) to move around as for short directions.  Use (north), (west), (east), and (south)"
      " for directions.  Type (look) to look for the description of a room.  Type (inventory) to check the item"
      " that you want to use.")
print()
print("You can battle an enemy by typing (battle).")
print()
print("To get an item, simply type (shop) in RUIN-1.")
print()
print("---------------------------------------------------------------------------------------------------")
print()


class Character(object):
    def __init__(self, character_name, health, inventory, coin, equip):
        self.name = character_name
        self.health = health
        self.inventory = inventory
        self.coin = coin
        self.equip = equip


class Name(Character):
    def __init__(self, character_name):
        super(Name, self). __init__(character_name, None, None, None, None)
        self.character_name = character_name
        name = ""


class Health(Character):
    def __init__(self, health):
        super(Health, self). __init__(None, health, None, None, None)

    health = 100
    if health == 0:
        print("You were killed.")
        quit(0)


class Inventory(Character):
    def __init__(self, inventory):
        super(Inventory, self). __init__(None, None, inventory, None, None)

    inventory = []


class Coins(Character):
    def __init__(self, coin):
        super(Coins, self). __init__(None, None, None, coin, None)

    coin_gold = 100


cc = Coins(0)


class Equip(Character):
    def __init__(self, equip):
        super(Equip, self). __init__(None, None, None, None, equip)


class Room(object):
    def __init__(self, name, north, west, east, south, up, down, look, battle_mode, evade, attack, shop, enemy, exit,):
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
        self.exit = exit

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, cost):
        super(Weapon, self). __init__(name)
        self.damage = damage
        self.cost = cost


class WoodenSword(Weapon):
    def __init__(self, name, damage, cost):
        super(WoodenSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


wooden_sword = WoodenSword("wooden sword", 5, None)


class StoneSword(Weapon):
    def __init__(self, name, damage, cost):
        super(StoneSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")

    cost = -25


stone_sword = StoneSword("stone sword", 15, -25)


class IronSword(Weapon):
    def __init__(self, name, damage, cost):
        super(IronSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


iron_sword = IronSword("iron sword", 25, 50)


class BoneSword(Weapon):
    def __init__(self, name, damage, cost):
        super(BoneSword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


bone_sword = BoneSword("bone sword", 40, 75)


class AxeOfFlame(Weapon):
    def __init__(self, name, damage, cost):
        super(AxeOfFlame, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


axe_of_flame = AxeOfFlame("axe of flame", 55, 100)


class ChillingSpear(Weapon):
    def __init__(self, name, damage, cost):
        super(ChillingSpear, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


chilling_spear = ChillingSpear("chilling spear", 65, 175)


class LegendarySword(Weapon):
    def __init__(self, name, damage, cost):
        super(LegendarySword, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


legendary_sword = LegendarySword("legendary sword", 80, 300)


class Lurker(Weapon):
    def __init__(self, name, damage, cost):
        super(Lurker, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


lurker = Lurker("lurker", 100, 400)


class FreezingRapier(Weapon):
    def __init__(self, name, damage, cost):
        super(FreezingRapier, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


freezing_rapier = FreezingRapier("freezing rapier", 135, 480)


class GreatAxe(Weapon):
    def __init__(self, name, damage, cost):
        super(GreatAxe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


great_axe = GreatAxe("great axe", 170, 560)


class Blazer(Weapon):
    def __init__(self, name, damage, cost):
        super(Blazer, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


blazer = Blazer("blazer", 230, 700)


class BigFlame(Weapon):
    def __init__(self, name, damage, cost):
        super(BigFlame, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


big_flame = BigFlame("big flame", 320, 900)


class LegendaryAxe(Weapon):
    def __init__(self, name, damage, cost):
        super(LegendaryAxe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


legendary_axe = LegendaryAxe("legendary axe", 450, 1500)


class InfinityScythe(Weapon):
    def __init__(self, name, damage, cost):
        super(InfinityScythe, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


infinity_scythe = InfinityScythe("infinity scythe", 600, 2000)


class ShadowBlade(Weapon):
    def __init__(self, name, damage, cost):
        super(ShadowBlade, self). __init__(name, damage, cost)
        self.dmg = damage
        self.cost = cost

    def attack(self):
        print("You attacked the enemy!")


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

    def drink(self):
        print("You drank the < HEALTH POTION >")


health_p = HealthP("health potion", 35, 25)


class SuperHealthP(Container):
    def __init__(self, name, health_give, cost):
        super(SuperHealthP, self). __init__(name, health_give, cost)

    def drink(self):
        print("You drank the < SUPER HEALTH POTION >")


super_health_p = SuperHealthP("super health potion", 50, 40)


class Food(Consumable):
    def __init__(self, name, health_give, cost):
        super(Food, self).__init__(name)
        self.health = health_give
        self.cost = cost


class Bread(Food):
    def __init__(self, name, health_give, cost):
        super(Bread, self). __init__(name, health_give, cost)
        self.health = health_give

    def eat(self):
        print("You ate the < BREAD >")


bread = Bread("bread", 20, 10)


class Apple(Food):
    def __init__(self, name, health_give, cost):
        super(Apple, self). __init__(name, health_give, cost)
        self.health = health_give

    def eat(self):
        print("You ate the < APPLE >")


apple = Apple("apple", 10, 5)


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

    def attack(self):
        print("The Sand Slime attacked!")

    def death(self):
        print("The Sand Slime was defeated...")

    health1 = 30

    coin1 = +2


ss = SandSlime("Sand Slime", 30, -2, +2)


class UndeadMummy(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(UndeadMummy, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Undead Mummy attacked!")

    def death(self):
        print("The Undead Mummy was defeated...")
        Coins.coin2 = +3

    health1 = 60

    coin1 = +3


um = UndeadMummy("Undead Mummy", 60, -5, 3)


class Skeleton(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Skeleton, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Skeleton attacked!")

    def death(self):
        print("The Skeleton was defeated...")

    health1 = 90

    coin1 = +4


s = Skeleton("Skeleton", 90, -3, 4)


class EyeShot(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(EyeShot, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Eye Shot attacked!")

    def death(self):
        print("The Eye Shot was defeated...")

    health1 = 50

    coin1 = +5


es = EyeShot("Eye Shot", 50, -15, 5)


class Carnage(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Carnage, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Carnage attacked!")

    def death(self):
        print("The Carnage was defeated...")

    health1 = 350

    coin1 = +5


c = Carnage("Carnage", 350, -6, 6)


class SuperMummy(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(SuperMummy, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Super Mummy attacked!")

    def death(self):
        print("The Super Mummy was defeated...")

    health1 = 500

    coin1 = +7


sm = SuperMummy("Super Mummy", 500, -5, 7)


class Destroyer(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Destroyer, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Destroyer attacked!")

    def death(self):
        print("The Destroyer was defeated...")

    health1 = 750

    coin1 = +9


d = Destroyer("Destroyer", 750, -3, 9)


class GoatMan(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(GoatMan, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Goat Man attacked!")

    def death(self):
        print("The Goat Man was defeated...")

    health1 = 1500

    coin1 = +13


gm = GoatMan("Goat Man", 1500, -10, 13)


class UndeadGolem(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(UndeadGolem, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Undead Golem attacked!")

    def death(self):
        print("The Undead Golem was defeated...")

    health1 = 2000

    coin1 = +25


ug = UndeadGolem("Undead Golem", 2000, -15, 25)


class ShadowDemon(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(ShadowDemon, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Shadow Demon attacked!")

    def death(self):
        print("The Shadow Demon was defeated...")

    health1 = 4000

    coin1 = +35


sd = ShadowDemon("Shadow Demon", 4000, -5, 35)


class Wraith(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Wraith, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("The Wraith attacked!")

    def death(self):
        print("The Wraith was defeated...")

    health1 = 8000

    coin1 = +0


w = Wraith("Wraith", 8000, -25, 0)


class Anubis(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(Anubis, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("Anubis attacked!")

    def death(self):
        print("Anubis was defeated...")

    health1 = 300000

    coin1 = +0


a = Anubis("Anubis", 300000, -10, 0)


class END(Enemies):
    def __init__(self, name, health, damage, coin_drop):
        super(END, self).__init__(name, health, damage, coin_drop)

    def attack(self):
        print("END attacked!")

    def death(self):
        print("END was defeated...")

    health1 = 5000

    coin1 = +0


e = END("END", 5000, -50, 0)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


shop_item = [StoneSword, IronSword, BoneSword, AxeOfFlame, ChillingSpear, LegendarySword, Lurker, FreezingRapier,
             GreatAxe, Blazer, BigFlame, LegendaryAxe, InfinityScythe, ShadowBlade, Apple, Bread, HealthP, SuperHealthP]

shop_itemNAMES = [" (1) Stone Sword", " (2) Iron Sword", " (3) Bone Sword", " (4) Axe Of Flame", " (5) Chilling Spear",
                  " (6) Legendary Sword", " (7) Lurker", " (8) Freezing Rapier", " (9) Great Axe", " (10) Blazer",
                  " (11) Big Flame", " (12) Legendary Axe", " (13) Infinity Scythe",
                  " (14) Shadow Blade", " (15) Apple", " (16) Bread", " (17) Health Potion",
                  " (18) Super Health Potion"]

guide = Room("Guide Room", "combat_training", None, None, None, None, None,
             "Hello and welcome to RUIN.  In this game, you'll be working your way to find the exit.  Go ahead and "
             "type in (north) or (n) to move onto the next place.", None, None, None, None, None, None)

combat_training = Room("Combat Training", None, None, None, None, None, "ruin1",
                       "In this area, you are going to experience a battle.  Simply type (battle), or go "
                       "ahead and press (down), or (d), to go in "
                       "the portal if you do not need the tutorial.", "battle1", None, None, None, None, None)

battle1 = Room("Battle Mode", None, None, None, None, None, "combat_training",
               "You entered a battle mode!  Type (evade) to avoid the attack.  You can attack by typing (attack). "
               " Take this wooden sword!  Type (down), or (d), to escape the battle.  There is a LVL 0  enemy.  "
               "< SAND SLIME >", None, "evade", "attack", None, SandSlime, None)

ruin1 = Room("RUIN-1", "ruin2", None, None, None, None, None,
             "Welcome to RUIN-1, this is where you can type (shop) to open the shop.  There's a room to the "
             "north.", None, None, None, "shop", None, None)

ruin2 = Room("RUIN-2", "ruin3", None, None, "ruin1", None, None,
             "You entered RUIN-2, there's a path to the north and south.  There is an enemy.",
             "battle2", None, None, None, None, None)

battle2 = Room("Battle Mode", None, None, None, None, None, "ruin2",
               "You entered battle mode!  There is a LVL 1 enemy.  < UNDEAD MUMMY >", None, "evade", "attack", None,
               UndeadMummy, None)

ruin3 = Room("RUIN-3", "ruin4", "grave1", None, "ruin3", None, None,
             "You entered RUIN-2, there's a path to the north and south.  There is an enemy.",
             "battle3", None, None, None, None, None)

grave1 = Room("Grave-1", None, None, "ruin3", None, None, None, "You entered a room, there's a grave and a path to the "
              " east.", None, None, None, None, None, None)

battle3 = Room("Battle Mode", None, None, None, None, None, "ruin3",
               "You entered battle mode!  There is a LVL 2 enemy.  < SKELETON >", None, "evade", "attack", None,
               Skeleton, None)

ruin4 = Room("RUIN-4", "ruin5", None, None, "ruin3", None, None,
             "You entered RUIN-4, there's a path to the north and south.  There is an enemy.",
             "battle4", None, None, None, None, None)

battle4 = Room("Battle Mode", None, None, None, None, None, "ruin4",
               "You entered battle mode!  There is a LVL 2 enemy.  < SKELETON >", None, "evade", "attack", None,
               Skeleton, None)

ruin5 = Room("RUIN-5", None, None, "ruin6", "ruin4", None, None,
             "You entered RUIN-5, there's a path to the east and south.  There is an enemy.",
             "battle5", None, None, None, None, None)

battle5 = Room("Battle Mode", None, None, None, None, None, "ruin5",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None,
               EyeShot, None)

ruin6 = Room("RUIN-6", None, "ruin5", "ruin7", None, None, None,
             "You entered RUIN-6, there's a path to the west and east.  There is an enemy.",
             "battle6", None, None, None, None, None)

battle6 = Room("Battle Mode", None, None, None, None, None, "ruin6",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None,
               EyeShot, None)

ruin7 = Room("RUIN-7", "grave2", "ruin6", "ruin8", None, None, None,
             "You entered RUIN-7, there's a path to the west and east.  There is an enemy.",
             "battle7", None, None, None, None, None)

grave2 = Room("Grave-2", None, None, None, "ruin7", None, None, "You entered a room, there's a grave and a path to the "
              " south.", None, None, None, None, None, None)

battle7 = Room("Battle Mode", None, None, None, None, None, "ruin7",
               "You entered battle mode!  There is a LVL 3 enemy.  < EYE SHOT >", None, "evade", "attack", None,
               EyeShot, None)

ruin8 = Room("RUIN-8", None, "ruin7", "ruin9", None, None, None,
             "You entered RUIN-8, there's a path to the west and east.  There is an enemy.",
             "battle8", None, None, None, None, None)

battle8 = Room("Battle Mode", None, None, None, None, None, "ruin8",
               "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None, Carnage,
               None)

ruin9 = Room("RUIN-9", None, "ruin8", None, "ruin10", None, None,
             "You entered RUIN-9, there's a path to the west and south.  There is an enemy.",
             "battle9", None, None, None, None, None)

battle9 = Room("Battle Mode", None, None, None, None, None, "ruin9",
               "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None, Carnage,
               None)

ruin10 = Room("RUIN-10", "ruin9", None, None, "ruin11", None, None,
              "You entered RUIN-10, there's a path to the north and south.  There is an enemy.",
              "battle10", None, None, None, None, None)

battle10 = Room("Battle Mode", None, None, None, None, None, "ruin10",
                "You entered battle mode!  There is a LVL 4 enemy.  < CARNAGE >", None, "evade", "attack", None,
                Carnage, None)

ruin11 = Room("RUIN-11", "ruin10", None, "grave3", "ruin12", None, None,
              "You entered RUIN-11, there's a path to the north and south.  There is an enemy.",
              "battle11", None, None, None, None, None)

grave3 = Room("Grave-3", None, "ruin11", None, None, None, None,
              "You entered a room, there's a grave and a path to the "
              " west.", None, None, None, None, None, None)

battle11 = Room("Battle Mode", None, None, None, None, None, "ruin11",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None,
                SuperMummy, None)

ruin12 = Room("RUIN-12", "ruin11", None, None, "ruin13", None, None,
              "You entered RUIN-12, there's a path to the north and south.  There is an enemy.",
              "battle12", None, None, None, None, None)

battle12 = Room("Battle Mode", None, None, None, None, None, "ruin12",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None,
                SuperMummy, None)

ruin13 = Room("RUIN-13", "ruin12", "ruin14", None, None, None, None,
              "You entered RUIN-13, there's a path to the north and west.  There is an enemy.",
              "battle13", None, None, None, None, None)

battle13 = Room("Battle Mode", None, None, None, None, None, "ruin13",
                "You entered battle mode!  There is a LVL 5 enemy.  < SUPER MUMMY >", None, "evade", "attack", None,
                SuperMummy, None)

ruin14 = Room("RUIN-14", None, "ruin15", "ruin13", None, None, None,
              "You entered RUIN-14, there's a path to the west and east.  There is an enemy.",
              "battle14", None, None, None, None, None)

battle14 = Room("Battle Mode", None, None, None, None, None, "ruin14",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer, None)

ruin15 = Room("RUIN-15", None, "ruin16", "ruin14", "grave4", None, None,
              "You entered RUIN-15, there's a path to the west and east.  There is an enemy.",
              "battle15", None, None, None, None, None)

grave4 = Room("Grave-4", "ruin15", None, None, None, None, None,
              "You entered a room, there's a grave and a path to the "
              " north.", None, None, None, None, None, None)

battle15 = Room("Battle Mode", None, None, None, None, None, "ruin15",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer, None)

ruin16 = Room("RUIN-16", "ruin17", None, "ruin15", None, None, None,
              "You entered RUIN-16, there's a path to the north and east.  There is an enemy.",
              "battle16", None, None, None, None, None)

battle16 = Room("Battle Mode", None, None, None, None, None, "ruin16",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer, None)

ruin17 = Room("RUIN-17", "ruin18", None, None, "ruin16", None, None,
              "You entered RUIN-17, there's a path to the north and south.  There is an enemy.",
              "battle16", None, None, None, None, None)

battle17 = Room("Battle Mode", None, None, None, None, None, "ruin17",
                "You entered battle mode!  There is a LVL 6 enemy.  < DESTROYER >", None, "evade", "attack", None,
                Destroyer, None)

ruin18 = Room("RUIN-18", "ruin19", None, None, "ruin17", None, None,
              "You entered RUIN-18, there's a path to the north and south.  There is an enemy.",
              "battle18", None, None, None, None, None)

battle18 = Room("Battle Mode", None, None, None, None, None, "ruin18",
                "You entered battle mode!  There is a LVL 7 enemy.  < GOAT MAN >", None, "evade", "attack", None,
                GoatMan, None)

ruin19 = Room("RUIN-19", None, None, "ruin20", "ruin18", None, None,
              "You entered RUIN-19, there's a path to the east and south.  There is an enemy.",
              "battle19", None, None, None, None, None)

battle19 = Room("Battle Mode", None, None, None, None, None, "ruin19",
                "You entered battle mode!  There is a LVL 7 enemy.  < GOAT MAN >", None, "evade", "attack", None,
                GoatMan, None)

ruin20 = Room("RUIN-20", None, "ruin19", "ruin21", None, None, None,
              "You entered RUIN-20, there's a path to the west and east.  There is an enemy.",
              "battle20", None, None, None, None, None)

battle20 = Room("Battle Mode", None, None, None, None, None, "ruin20",
                "You entered battle mode!  There is a LVL 8 enemy.  < UNDEAD GOLEM >", None, "evade", "attack", None,
                UndeadGolem, None)

ruin21 = Room("RUIN-21", None, "ruin20", None, "ruin22", None, None,
              "You entered RUIN-21, there's a path to the west and south.  There is an enemy.",
              "battle21", None, None, None, None, None)

battle21 = Room("Battle Mode", None, None, None, None, None, "ruin21",
                "You entered battle mode!  There is a LVL 8 enemy.  < UNDEAD GOLEM >", None, "evade", "attack", None,
                UndeadGolem, None)

ruin22 = Room("RUIN-22", "ruin21", None, None, "ruin23", None, None,
              "You entered RUIN-22, there's a path to the north and south.  There is an enemy.",
              "battle22", None, None, None, None, None)

battle22 = Room("Battle Mode", None, None, None, None, None, "ruin22",
                "You entered battle mode!  There is a LVL 9 enemy.  < SHADOW DEMON >", None, "evade", "attack", None,
                ShadowDemon, None)

ruin23 = Room("RUIN-23", "ruin22", "battle24", None, None, None, None,
              "You entered RUIN-23, there's a path to the north and west.  There is an enemy.",
              "battle23", None, None, None, None, None)

battle23 = Room("Battle Mode", None, None, None, None, None, "ruin23",
                "You entered battle mode!  There is a LVL 9 enemy.  < SHADOW DEMON >", None, "evade", "attack", None,
                ShadowDemon, None)

battle24 = Room("Battle Mode", None, None, None, None, None, None,
                "You entered battle mode!  The boss has closed the entrance you came from, you will not be able to "
                "escape...  There is a LVL 10 enemy.  < WRAITH >", None, "evade", "attack", None, Wraith, None)

ruin24 = Room("RUIN-24", "end", None, "ruin23", None, None, None,
              "You entered RUIN-24, there's a path to the north and east.  You see the corpse of the WRAITH near you.",
              None, None, None, None, None, None)

end = Room("END", None, None, None, None, "exit0", "endBOSS", "You entered the END, there's a ladder which leads up.",
           None, None, None, None, None, None)

exit0 = Room("Escaped...", None, None, None, None, None, None, "You exit from the ground.  You walked away from the "
             "place you came from, and you were never seen again, but you became a legend.", None, None, None, None,
             None, None)

endBOSS = Room("Battle Mode", None, None, None, None, None, "end",
               "You entered battle mode...  There is an enemy.  < END >", None, "evade", "attack", None, END, None)

shop = Room("Forgotten Shop", None, None, None, None, None, None,
            "Welcome to the shop.  You will have to battle enemies to get enough money "
            "to buy an item.  Type (exit) to exit the shop.  To see the items the details of an item,"
            " simply type (details).  To buy an item, type (buy).",
            None, None, None, "shop", None, "ruin1")


battleANUBIS = Room("UNDERWORLD", None, None, None, None, None, None,
                    "You entered battle mode!  There is an enemy.  < ANUBIS >", None, "evade", "attack", None, Anubis,
                    None)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


current_node = guide
DIRECTIONS = ["north", "east", "south", "west", "up", "down", "battle", "shop", "exit"]
short_directions = ["n", "e", "s", "w", "u", "d"]

while True:
    print("Current Location: %s" % current_node.name)
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
        print(Inventory.inventory)
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

    if grave2 == current_node:
        if command == "hit grave":
            print("ANUBIS:  You shouldn't have done that...  ( ANUBIS ATTACKS! )")
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            current_node = battleANUBIS

    if grave3 == current_node:
        if command == "hit grave":
            print("ANUBIS:  You shouldn't have done that...  ( ANUBIS ATTACKS! )")
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            current_node = battleANUBIS

    if grave4 == current_node:
        if command == "hit grave":
            print("ANUBIS:  You shouldn't have done that...  ( ANUBIS ATTACKS! )")
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            current_node = battleANUBIS

    if exit0 == current_node:
        exit(0)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    damage = "The Sand Slime attacked!"
    avoid = "The Sand Slime avoided your attack!"
    enemy_option = [damage, avoid]
    if damage == random.randrange(len(enemy_option)):
        print(damage)
        print("Your health is at %d." % Health.health)
        Health.health -= 2

    if avoid == random.randrange(len(enemy_option)):
        print(avoid)
        SandSlime.health1 += 5

    if battle1 == current_node:
        if command == "evade":
            print("You are planning to avoid the enemy's attack...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("The Sand Slime attacked!")
            print("It missed!")
            print("Your health is at %d." % Health.health)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
        if command == "attack":
            print("You are planning to attack the enemy...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("You attacked the enemy!")
            SandSlime.health1 -= 5
            rand_option = enemy_option[random.randrange(len(enemy_option))]
            if rand_option == damage:
                print(damage)
                Health.health -= 2
                print("The health of the Sand Slime is at %d." % SandSlime.health1)
                print("Your health is at %d." % Health.health)
            if rand_option == avoid:
                print(avoid)
                SandSlime.health1 += 5
                print("The health of the Sand Slime is at %d." % SandSlime.health1)
                print("Your health is at %d." % Health.health)

            if SandSlime.health1 <= 0:
                ss.death()
                SandSlime.coin1 += Coins.coin_gold
                print("You got %d coins." % ss.coin_drop)
                current_node = ruin1
                print()
                print("-------------------------------------------------------------------------------------------")
                print()
                print("Congratulations, you beat the Sand Slime.  You now know how to battle enemies and defeat "
                      "them")
                SandSlime.health1 += 30

            if Health.health <= 0:
                print("You were killed.")
                quit(0)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    damage1 = "The Undead Mummy attacked!"
    avoid1 = "The Undead Mummy avoided your attack!"
    enemy_option1 = [damage1, avoid1]
    if damage1 == random.randrange(len(enemy_option1)):
        print(damage1)
        print("Your health is at %d." % Health.health)
        Health.health -= 5

    if avoid1 == random.randrange(len(enemy_option1)):
        print(avoid1)
        UndeadMummy.health1 += 5

    if battle2 == current_node:
        if command == "evade":
            print("You are planning to avoid the enemy's attack...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("The Undead Mummy attacked!")
            print("It missed!")
            print("Your health is at %d." % Health.health)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
        if command == "attack":
            print("You are planning to attack the enemy...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("You attacked the enemy!")
            UndeadMummy.health1 -= 5
            rand_option = enemy_option1[random.randrange(len(enemy_option1))]
            if rand_option == damage1:
                print(damage1)
                Health.health -= 5
                print("The health of the Undead Mummy is at %d." % UndeadMummy.health1)
                print("Your health is at %d." % Health.health)
            if rand_option == avoid1:
                print(avoid1)
                UndeadMummy.health1 += 5
                print("The health of the Undead Mummy is at %d." % UndeadMummy.health1)
                print("Your health is at %d." % Health.health)

            if UndeadMummy.health1 <= 0:
                um.death()
                UndeadMummy.coin1 += Coins.coin_gold
                print("You got %d coins." % um.coin_drop)
                print()
                print("-------------------------------------------------------------------------------------------")
                print()
                UndeadMummy.health1 += 60

            if Health.health <= 0:
                print("You were killed.")
                quit(0)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    damage2 = "The Skeleton attacked!"
    avoid2 = "The Skeleton avoided your attack!"
    enemy_option2 = [damage2, avoid2]
    if damage2 == random.randrange(len(enemy_option2)):
        print(damage2)
        print("Your health is at %d." % Health.health)
        Health.health -= 3

    if avoid2 == random.randrange(len(enemy_option2)):
        print(avoid2)
        Skeleton.health1 += 5

    if battle3 == current_node:
        if command == "evade":
            print("You are planning to avoid the enemy's attack...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("The Skeleton attacked!")
            print("It missed!")
            print("Your health is at %d." % Health.health)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
        if command == "attack":
            print("You are planning to attack the enemy...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("You attacked the enemy!")
            Skeleton.health1 -= 5
            rand_option = enemy_option2[random.randrange(len(enemy_option2))]
            if rand_option == damage2:
                print(damage2)
                Health.health -= 3
                print("The health of the Undead Mummy is at %d." % Skeleton.health1)
                print("Your health is at %d." % Health.health)
            if rand_option == avoid2:
                print(avoid2)
                Skeleton.health1 += 5
                print("The health of the Skeleton is at %d." % Skeleton.health1)
                print("Your health is at %d." % Health.health)

            if Skeleton.health1 <= 0:
                s.death()
                Skeleton.coin1 += Coins.coin_gold
                print("You got %d coins." % s.coin_drop)
                print()
                print("-------------------------------------------------------------------------------------------")
                print()
                Skeleton.health1 += 60

            if Health.health <= 0:
                print("You were killed.")
                quit(0)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    damage3 = "The Skeleton attacked!"
    avoid3 = "The Skeleton avoided your attack!"
    enemy_option3 = [damage3, avoid3]
    if damage3 == random.randrange(len(enemy_option3)):
        print(damage3)
        print("Your health is at %d." % Health.health)
        Health.health -= 3

    if avoid3 == random.randrange(len(enemy_option3)):
        print(avoid3)
        Skeleton.health1 += 5

    if battle4 == current_node:
        if command == "evade":
            print("You are planning to avoid the enemy's attack...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("The Skeleton attacked!")
            print("It missed!")
            print("Your health is at %d." % Health.health)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
        if command == "attack":
            print("You are planning to attack the enemy...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time
            time.sleep(3)

            print("You attacked the enemy!")
            Skeleton.health1 -= 5
            rand_option = enemy_option3[random.randrange(len(enemy_option3))]
            if rand_option == damage3:
                print(damage3)
                Health.health -= 3
                print("The health of the Skeleton is at %d." % Skeleton.health1)
                print("Your health is at %d." % Health.health)
            if rand_option == avoid3:
                print(avoid3)
                Skeleton.health1 += 5
                print("The health of the Skeleton is at %d." % Skeleton.health1)
                print("Your health is at %d." % Health.health)

            if Skeleton.health1 <= 0:
                s.death()
                Skeleton.coin1 += Coins.coin_gold
                print("You got %d coins." % s.coin_drop)
                print()
                print("-------------------------------------------------------------------------------------------")
                print()
                Skeleton.health1 += 60

            if Health.health <= 0:
                print("You were killed.")
                quit(0)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    damage4 = "The Eye Shot attacked!"
    avoid4 = "The Eye Shot avoided your attack!"
    enemy_option4 = [damage4, avoid4]
    if damage4 == random.randrange(len(enemy_option4)):
        print(damage4)
        print("Your health is at %d." % Health.health)
        Health.health -= 15

    if avoid4 == random.randrange(len(enemy_option4)):
        print(avoid4)
        EyeShot.health1 += 5

    if battle5 == current_node:
        if command == "evade":
            print("You are planning to avoid the enemy's attack...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time

            time.sleep(3)

            print("The Eye Shot attacked!")
            print("It missed!")
            print("Your health is at %d." % Health.health)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
        if command == "attack":
            print("You are planning to attack the enemy...")
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()
            import time

            time.sleep(3)

            print("You attacked the enemy!")
            EyeShot.health1 -= 5
            rand_option = enemy_option4[random.randrange(len(enemy_option4))]
            if rand_option == damage4:
                print(damage4)
                Health.health -= 15
                print("The health of the Eye Shot is at %d." % EyeShot.health1)
                print("Your health is at %d." % Health.health)
            if rand_option == avoid4:
                print(avoid4)
                EyeShot.health1 += 5
                print("The health of the Eye Shot is at %d." % EyeShot.health1)
                print("Your health is at %d." % Health.health)

            if EyeShot.health1 <= 0:
                es.death()
                EyeShot.coin1 += Coins.coin_gold
                print("You got %d coins." % um.coin_drop)
                print()
                print("-------------------------------------------------------------------------------------------")
                print()
                EyeShot.health1 += 50

            if Health.health <= 0:
                print("You were killed.")
                quit(0)
            print()
            print("-----------------------------------------------------------------------------------------------")
            print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        damage5 = "The Skeleton attacked!"
        avoid5 = "The Skeleton avoided your attack!"
        enemy_option5 = [damage5, avoid5]
        if damage5 == random.randrange(len(enemy_option5)):
            print(damage5)
            print("Your health is at %d." % Health.health)
            Health.health -= 5

        if avoid4 == random.randrange(len(enemy_option5)):
            print(avoid4)
            UndeadMummy.health1 += 5

        if battle6 == current_node:
            if command == "evade":
                print("You are planning to avoid the enemy's attack...")
                print()
                print("-----------------------------------------------------------------------------------------------")
                print()
                import time

                time.sleep(3)

                print("The Skeleton attacked!")
                print("It missed!")
                print("Your health is at %d." % Health.health)
                print()
                print("-----------------------------------------------------------------------------------------------")
                print()
            if command == "attack":
                print("You are planning to attack the enemy...")
                print()
                print("-----------------------------------------------------------------------------------------------")
                print()
                import time

                time.sleep(3)

                print("You attacked the enemy!")
                Skeleton.health1 -= 5
                rand_option = enemy_option5[random.randrange(len(enemy_option5))]
                if rand_option == damage5:
                    print(damage5)
                    Health.health -= 2
                    print("The health of the Skeleton is at %d." % Skeleton.health1)
                    print("Your health is at %d." % Health.health)
                if rand_option == avoid5:
                    print(avoid5)
                    Skeleton.health1 += 5
                    print("The health of the Skeleton is at %d." % Skeleton.health1)
                    print("Your health is at %d." % Health.health)

                if Skeleton.health1 <= 0:
                    um.death()
                    Skeleton.coin1 += Coins.coin_gold
                    print("You got %d coins." % um.coin_drop)
                    print()
                    print("-------------------------------------------------------------------------------------------")
                    print()
                    Skeleton.health1 += 60

                if Health.health <= 0:
                    print("You were killed.")
                    quit(0)
                print()
                print("-----------------------------------------------------------------------------------------------")
                print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if shop == current_node:
        if command == "details":

            print("SHOP ITEM DETAILS:")
            print(shop_itemNAMES)
            print()
            print("Stone Sword:  < damage: 15 >, < cost: 25 >")
            print()
            print("Iron Sword:  < damage: 25 >, < cost: 50 >")
            print()
            print("Bone Sword:  < damage: 40 >, < cost: 75 >")
            print()
            print("Axe Of Flame:  < damage: 55 >, < cost: 100 >")
            print()
            print("Chilling Spear:  < damage: 65 >, < cost: 175 >")
            print()
            print("Legendary Sword:  < damage: 80 >, < cost: 300 >")
            print()
            print("Lurker:  < damage: 100 >, < cost: 400 >")
            print()
            print("Freezing Rapier:  < damage: 135 >, < cost: 480 >")
            print()
            print("Great Axe:  < damage: 160 >, < cost: 560 >")
            print()
            print("Blazer:  < damage: 230 >, < cost: 700 >")
            print()
            print("Big Flame:  < damage: 320 >, < cost: 900 >")
            print()
            print("Legendary Axe:  < damage: 450 >, < cost: 1500 >")
            print()
            print("Infinity Scythe:  < damage: 600 >, < cost: 2000 >")
            print()
            print("Shadow Blade:  < damage: 1000 >, < cost: 3000 >")
            print()
            print("Apple:  < health gain: 5 >, < cost: 5 >")
            print()
            print("Bread:  < health gain: 15 >, < cost: 15 >")
            print()
            print("Health Potion:  < health gain: 25 >, < cost: 25 >")
            print()
            print("Super Health Potion:  < health gain: 50 >, < cost: 50 >")
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()

    if shop == current_node:
        if command == "buy":
            print("SHOP ITEM:")
            print(shop_itemNAMES)

            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            print("You have %d coins." % Coins.coin_gold)
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            user_choice = str(input("SHOP KEEPER:  What do you want?  CHAT:  >_"))
            print()
            print("---------------------------------------------------------------------------------------------------")
            print()
            shop_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                            "18"]
            if user_choice == "1":
                if Coins.coin_gold >= stone_sword.cost:
                    stone_sword.cost -= Coins.coin_gold
                    print("You bought the < STONE SWORD >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "2":
                if Coins.coin_gold >= iron_sword.cost:
                    print("You bought the < IRON SWORD >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "3":
                if Coins.coin_gold >= bone_sword.cost:
                    print("You bought the < BONE SWORD >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "4":
                if Coins.coin_gold >= axe_of_flame.cost:
                    print("You bought the < AXE OF FLAME >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "5":
                if Coins.coin_gold >= chilling_spear.cost:
                    print("You bought the < CHILLING SPEAR >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "6":
                if Coins.coin_gold >= legendary_axe.cost:
                    print("You bought the < LEGENDARY >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "7":
                if Coins.coin_gold >= lurker.cost:
                    print("You bought the < LURKER >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "8":
                if Coins.coin_gold >= freezing_rapier.cost:
                    print("You bought the < FREEZING RAPIER >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "9":
                if Coins.coin_gold >= great_axe.cost:
                    print("You bought the < GREAT AXE >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "10":
                if Coins.coin_gold >= blazer.cost:
                    print("You bought the < BLAZER >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "11":
                if Coins.coin_gold >= big_flame.cost:
                    print("You bought the < BIG FLAME >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "12":
                if Coins.coin_gold >= legendary_axe.cost:
                    print("You bought the < LEGENDARY AXE >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "13":
                if Coins.coin_gold >= infinity_scythe.cost:
                    print("You bought the < INFINITY SCYTHE >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "14":
                if Coins.coin_gold >= shadow_blade.cost:
                    print("You bought the < SHADOW BLADE >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "15":
                if Coins.coin_gold >= apple.cost:
                    print("You bought the < APPLE >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "16":
                if Coins.coin_gold >= bread.cost:
                    print("You bought the < BREAD >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "17":
                if Coins.coin_gold >= health_p.cost:
                    print("You bought the < HEALTH POTION >.")
                else:
                    print("You cannot buy that.")

            if user_choice == "18":
                if Coins.coin_gold >= super_health_p.cost:
                    print("You bought the < SUPER HEALTH POTION >.")
                else:
                    print("You cannot buy that.")
            print()
            print("---------------------------------------------------------------------------------------------------")
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
