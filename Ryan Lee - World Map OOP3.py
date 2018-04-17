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
               "You're outside of a house; there's a garden to the east and a shelter to the west.")
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
               "You entered a kitchen and there's something on the table.")
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
        quit(0)  # ADD THIS CODE TO NOT REPEAT!!!
    elif command in short_directions:
        position = short_directions.index(command)
        command = DIRECTIONS[position]
    if command in DIRECTIONS:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
            print()