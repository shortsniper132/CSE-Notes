class Character(object):
    def __init__(self, name, status, take_damage, pick_up_items, status_effect):
        self.name = name
        self.health_status = status
        self.dmg = take_damage
        self.inventory = pick_up_items
        self.status = status_effect


def player_name(self):
    self.name = "Rook"

    name = "TEST"
    print("You're character's name is %s." % name)


def status(self):
    poison = "You're slowly losing health."
    health_status = 0
    print(poison)
    if health_status == 0:
        print("You died from poison.")
        quit(0)


def health(self):
    self.health_status = 100

    health_status = 100
    print("You have %d health." % health_status)
    if health_status == 0:
        print("You perished.")
        quit(0)


def damage(self):
    self.damage()


def pick(self):
    self.inventory()


inventory = 0
if inventory == 15:
    print("You cannot pick anymore items.")
    inventory = 0
    print("You picked up the item.")
    print(1 + + inventory)
