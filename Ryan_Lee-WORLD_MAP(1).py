print("HINT: Be sure all of your words are UPPERCASE.")
print(" ")
print("Starting...")
print(" ")
world_map = {
    "OUTSIDE HOUSE": {
        "NAME": "Outside of House",
        "DESCRIPTION": "You are outside of your house, you see a garden to the east, a door to the north"
                       " which leads inside of your house to the north, and a shelter to your west.",
        "LOOK": "You see a no items near your location.",
        "PATHS": {
            "NORTH": "ROOM 1",
            "WEST": "SHELTER",
            "EAST": "GARDEN",
        }
    },
    "SHELTER": {
        "NAME": "Shelter",
        "DESCRIPTION": "You're at the door of the shelter and you need a password to get in.",
        "LOOK": "You see a door in front of you.",
        "PATHS": {
            "WEST": "INSIDE OF SHELTER",
            "EAST": "OUTSIDE HOUSE",
        }
    },
    "GARDEN": {
        "NAME": "Beautiful Garden",
        "DESCRIPTION": "You're next to your garden and you see a watering can and shovel and lots of flowers.",
        "LOOK": "You see pretty flowers.",
        "PATHS": {
            "WEST": "OUTSIDE HOUSE",
            "DOWN": "SECRET WORLD"
        }
    },
    "ROOM 1": {
        "NAME": "Room 1 - House",
        "DESCRIPTION": "You entered your home and you have a path to the north and a door to the east and south; there"
                       " is also a table with items.",
        "LOOK": "You see a hammer and a screwdriver on the table.",
        "PATHS": {
            "NORTH": "ROOM 2",
            "EAST": "CLOSET",
            "SOUTH": "OUTSIDE HOUSE"
        }
    },
    "ROOM 2": {
        "NAME": "Room 2 - House",
        "DESCRIPTION": "You entered the next room and you see your cat.  There seems to be a path to the west which"
                       " leads to the kitchen and a path to the north and south.",
        "LOOK": "There's multiple paths as you look around.",
        "PATHS": {
            "NORTH": "HALLWAY 1",
            "WEST": "KITCHEN",
            "SOUTH": "ROOM 1",
        }

    },
    "CLOSET": {
        "NAME": "Closet",
        "DESCRIPTION": "You opened your closet which was filled with items.",
        "LOOK": "You see a closet filled with items.",
        "PATHS": {
            "WEST": "ROOM 1",
            "EAST": "SECRET ROOM"  # If pulled trigger = ROOM
        }
    },
    "SECRET ROOM": {
        "NAME": "SECRET ROOM",
        "DESCRIPTION": "You entered the secret room and you see more items, there's also a robotic leg.",
        "LOOK": "You see a room with lots of scrap metal.",
        "PATHS": {
            "WEST": "CLOSET",
        }
    },
    "KITCHEN": {
        "NAME": "Enchanting Kitchen",
        "DESCRIPTION": "You are in a kitchen, but there is nothing except a table, chair, oven, fridge, and counter.",
        "LOOK": "You see a table, chair, oven, fridge, and counter.",
        "PATHS": {
            "EAST": "ROOM 2",
        }
    },
    "HALLWAY 1": {
        "NAME": "Hallway of Rooms",
        "DESCRIPTION": "You're in a hallway and there is 2 rooms for you to go in, there is also stairs to the north.",
        "LOOK": "You see 2 rooms you can go, there seems to be a boulder to the north behind the ladder; the boulder"
                " seems to appear even though it is moved, it must be magical.",
        "PATHS": {
            "SOUTH": "ROOM 2",
            "WEST": "BEDROOM 1",
            "EAST": "BEDROOM 2",
            "NORTH": "HOUSE F2",
            "DOWN": "BASEMENT"  # TOOL = MOVE BOULDER
        }
    },
    "BEDROOM 1": {
        "NAME": "Red Bedroom",
        "DESCRIPTION": "You entered a bedroom with multiple furniture.",
        "LOOK": "You see a ladder.",
        "PATHS": {
            "EAST": "HALLWAY 1",
        }
    },
    "BEDROOM 2": {
        "NAME": "Blue Bedroom",
        "DESCRIPTION": "You entered a bedroom with multiple furniture.",
        "LOOK": "You see a backpack and fruit.",
        "PATHS": {
            "WEST": "HALLWAY 1"
        }
    },
    "INSIDE OF SHELTER": {
        "NAME": "Shelter Interior",
        "DESCRIPTION": "You entered the shelter and it has a robotic arm and a workspace"
                       " that seems you can build to the north.",
        "LOOK": "You see a path to the north and a door to the east and nothing for you to use on the floor.",
        "PATHS": {
            "NORTH": "CRAFT",
            "EAST": "SHELTER",
        }
    },
    "CRAFT": {
        "NAME": "Crafting Station UB1",
        "DESCRIPTION": "You are at the crafting station, it seems you can build anything, but you need the tools and"
                       " items.  The robot you see in front of you is half complete; it's unlikely it will be"
                       " hostile or not.",
        "LOOK": "You see a crafting station and a robot.",
        "PATHS": {
            "SOUTH": "INSIDE OF SHELTER",
        }
    },
    "HOUSE F2": {
        "NAME": "F2 ROOM - House",
        "DESCRIPTION": "You went up the stairs and you see a ladder leading up to an attic.",
        "LOOK": "The only way is to go up or back down the stairs, there's no other rooms;"
                " there's also a bag on the floor.",
        "PATHS": {
            "UP": "ATTIC",
            "SOUTH": "HALLWAY 1"
        }
    },
    "ATTIC B1": {
        "NAME": "Attic of Silence",
        "DESCRIPTION": "You entered the attic and you see many old furniture.",
        "LOOK": "You see a rug, chair, tool, lamp, and a window.  You also see a robotic body.",
        "PATHS": {
            "DOWN": "HOUSE F2",
            "NORTH": "ATTIC B2"
        }
    },
    "ATTIC B2": {
        "NAME": "Attic of Silence's Window",
        "DESCRIPTION": "You moved to the north and you are next to the window.",
        "LOOK": "You see your car and an endless road through the window.",
        "PATHS": {
            "DOWN": "FRONT HOUSE",
        }
    },
    "FRONT HOUSE": {
        "NAME": "Front of House",
        "DESCRIPTION": "You jumped down from the window and you unexpectedly survived the fall.",
        "LOOK": "You see your car and an endless road in front of your house, but your car has no gas and it is"
                " locked, only if you dropped items before you jumped.",
        "PATHS": {
            "NORTH": "ROAD"
        }
    },
    "ROAD": {
        "NAME": "ENDLESS ROAD",
        "DESCRIPTION": "You went to the road and you walked endlessly without any supplies..."
                       " you perished...",  # YOU PERISHED = GAME END
    },
    "SECRET WORLD": {
        "NAME": "Secret World",
        "DESCRIPTION": "You appeared in a world with fire and evil.",
        "LOOK": "You see a world with fire and you are surrounded by dark fog.",
        "PATHS": {
            "NORTH": "SECRET WORLD B1",
        }
    },
    "SECRET WORLD B1": {
        "NAME": "Secret World",
        "DESCRIPTION": "You went to the north and you see a figure and it was guarding the gates to flame."
                       " It is likely that you won't beat the figure.",
        "LOOK": "You see a gate that's guarded by a figure.",
        "PATHS": {
            "NORTH": "GATES",
            "SOUTH": "SECRET WORLD",
        }
    },
    "GATES": {
        "NAME": "Secret World Gates",
        "DESCRIPTION": "You walked toward the gates and you were stopped by the figure.",
        "LOOK": "You see a figure in front of you.",
        "PATHS": {
            "NORTH": "GATES 2",
            "SOUTH": "SECRET WORLD B1",
        }
    },
    "GATES 2": {
        "NAME": "Secret World Gates",
        "DESCRIPTION": "You did not hesitate and you kept walking, but the figure ate you as if you were not welcomed."
                       " You were eaten...",
    },
    "BASEMENT": {
        "NAME": "Basement - 1",
        "DESCRIPTION": "You appeared in the basement's main room.",
        "LOOK": "You see nothing, but you feel a chill go down your back, you seem terrified.",
        "PATHS": {
            "NORTH": "BASEMENT 2",
            "WEST": "BASEMENT 3",
            "EAST": "BASEMENT 4",
            "UP": "HALLWAY 1"
        }
    },
    "BASEMENT 2": {
        "NAME": "Basement - 2",
        "DESCRIPTION": "You moved to the north and you appeared in another room.",
        "LOOK": "You hear a noise as you stood still.",
        "PATHS": {
            "SOUTH": "BASEMENT",
        }
    },
    "BASEMENT 3": {
        "NAME": "Basement - 3",
        "DESCRIPTION": "You moved to the west and you appeared in another room.",
        "LOOK": "You hear a noise.",
        "PATHS": {
            "EAST": "BASEMENT",
        }
    },
    "BASEMENT 4": {
        "NAME": "Basement - 4",
        "DESCRIPTION": "You moved to the east and you appeared in another room.",
        "LOOK": "You felt water as you moved to the east.",
        "PATHS": {
            "EAST": "BASEMENT - 5",
        }
    },
    "BASEMENT 5": {
        "NAME": "Basement - 5",
        "DESCRIPTION": "You moved more to the east and you heard a growl.",
        "LOOK": "You heard the noise closer as you went further.",
        "PATHS": {
            "EAST": "BASEMENT",
        }
    },
    "BASEMENT 6": {
        "NAME": "Basement - 6",
        "DESCRIPTION": "You moved more to the east and you were eaten by a figure, you perished...",
    },
}

current_node = world_map["OUTSIDE HOUSE"]
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST", "UP", "DOWN"]
while True:
    print("LOCATION: %s." % current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command == "LOOK":
        print(" ")
        print(current_node["LOOK"])
        print(" ")
    if command == "QUIT":
        quit(0)  # ADD THIS CODE TO NOT REPEAT!!!
    if command in DIRECTIONS:
        try:
            name_of_node = current_node["PATHS"][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
