class OutsideOfHouse(object):
    def __init__(self, name, north, west, east, look):
        self.name = name
        self.north = north
        self.west = west
        self.east = east
        self.look = look
    look = "You're outside of a house; there's a garden to the east and a shelter to the west."

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Shelter(object):
    def __init__(self, name, west, east, look):
        self.name = name
        self.west = west
        self.east = east
        self.look = look

    def move(self, direction):
            global current_node
            current_node = globals()[getattr(self, direction)]


class Garden(object):
    def __init__(self, name, west, look):
            self.name = name
            self.west = west
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class EntranceOfHouse(object):
    def __init__(self, name, north, south, east, look):
            self.name = name
            self.north = north
            self.east = east
            self.south = south
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Hallway1(object):
    def __init__(self, name, north, west, south, look):
            self.name = name
            self.north = north
            self.west = west
            self.south = south
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Kitchen(object):
    def __init__(self, name, east, look):
            self.name = name
            self.east = east
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Closet(object):
    def __init__(self, name, west, east, look):
            self.name = name
            self.west = west
            self.east = east
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class InsideOfShelter(object):
    def __init__(self, name, north, east, look):
            self.name = name
            self.north = north
            self.east = east
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class SecretB1(object):
    def __init__(self, name, west, look):
            self.name = name
            self.west = west
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Hallway2(object):
    def __init__(self, name, north, west, east, south, look):
            self.name = name
            self.north = north
            self.west = west
            self.east = east
            self.south = south
            self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Lookout(object):
    def __init__(self, name, up, south, look):
        self.name = name
        self.up = up
        self.south = south
        self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class HallwayRoom1(object):
    def __init__(self, name, west, look):
        self.name = name
        self.west = west
        self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class HallwayRoom2(object):
    def __init__(self, name, east, look):
        self.name = name
        self.east = east
        self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class AtticR1(object):
    def __init__(self, name, north, down, look):
        self.name = name
        self.north = north
        self.down = down
        self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class AtticR2(object):
    def __init__(self, name, south, look):
        self.name = name
        self.south = south
        self.look = look

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


current_node = OutsideOfHouse
DIRECTIONS = ["north", "east", "south", "west", "up", "down"]
short_directions = ["n", "e", "s", "w", "u", "d"]

while True:
    print(current_node.name)
    print("")
    command = input("CHAT: >_").lower().strip()
    print("")
    if command == "look":
        print(current_node.look)
    print(" ")
    if command == "quit":
        quit(0)  # ADD THIS CODE TO NOT REPEAT!!!
    elif command in short_directions:
        position = short_directions.index(command)
        command = DIRECTIONS[position]
    if command in DIRECTIONS:
        try:
            name_of_node = current_node
            print("You moved...")
            print(" ")

            def move(self, direction):
                global current_node
                current_node = globals()[getattr(self, direction)]
        except KeyError:
            print("You cannot go this way.")
