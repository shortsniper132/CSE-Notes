# Must have:
# Health
# Pick up items
# Move?
# Attack
# Death
# Dialogue
# Name
# Perform action
# Description
# Status effect
# Take damage


# Assignment:  CREATE A CHARACTER CLASS AND MUST HAVE FIVE INSTANCE VARIABLES  instance variables = (self.)
# All five instance variables MUST be used.  It must also have two methods and a constructor. constructor = def __init__

class Enemy(object):
        def __init__(self, character, attack):
            self.goblin = character
            self.dmg = attack
            print("There is a %s." % attack)
            attack = -10
            print("The enemy attacked, you lost %s health." % attack)


enemy_desc = Enemy
print(Enemy)


while True:
    command = input("CHAT: >_").lower().strip()


    class Character(object):
        def __init__(self, name, status, take_damage, pick_up_items, status_effect):
            self.name = name
            self.health_status = status
            self.dmg = take_damage
            self.inventory = pick_up_items
            self.status = status_effect

        def player_name(self):
            self.name = "Rook"
        if command == "name":
            name = "Rook"
            print("You're character's name is %s." % name)

        def health(self):
            self.health_status = 100
        if command == "health":
            health_status = 100
            print("You have %d health." % health_status)
            if health_status == 0:
                print("You perished.")
                quit(0)

        def damage(self):
            self.damage()
        if Enemy:
            attack = True
            health_status = attack

        def pick(self):
            self.inventory()
        inventory = 0
        if inventory == 15:
            print("You cannot pick anymore items.")

        if command == "pick up":
            inventory = 0

            print("You picked up the item.")
            print(1 + + inventory)

        def status(self):
            self.status = True
        if command == "poison":
            while True:
                poison = "You're slowly losing health."
                health_status = 0
                print(poison)
                if health_status == 0:
                    print("You died from poison.")
                    quit(0)
        if command == "heal":
            print("You got cured from poison.")
