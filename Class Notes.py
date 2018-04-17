# Defining a class
class Cheeseburger(object):  # Capitalized because (C) in Cheeseburger is an object.
    def __init__(self, patty, cheese):  # TWO underscores before and after
        self.patty = patty
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful and eats the cheeseburger.")

    def cut(self):
        print("You cut the cheeseburger.")

    def eat(self):
        print("You eat the cheeseburger...")
        self.eaten = True


# Instantiating (The creation of) two cheeseburgers
burger1 = Cheeseburger("Beef", "Havarti")
burger2 = Cheeseburger("Bacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)  # Prints out what cheese it has.

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)


class Car(object):
    def __init__(self, name, color, num_of_doors, hp):  # Doesn't have to be in order; be in order to be easier.
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("Nothing Happens.")
        else:
            self.running = True
            print("The car starts.")

    def move_forward(self):
        if self.running:
            print("You move forward.")
        else:
            print("Nothing Happens.")

    def turn_off(self):
        if self.running:
            self.running = True
            print("You turn the car off.")
        else:
            print("The car is already off.")

    def go_for_drive(self, passengers):
        print("%d passengers get in." % passengers)
        self.passengers = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out." % passengers)
        self.passengers = 0


my_car = Car("Normal Car", "Black", 2, 100)

my_car.go_for_drive(1)


# A car can move, blow up, it can not move, it can be transformed (sci fi), a car can open doors and windows.  A
# car can also accelerate, and can wipe windows on the front window of the car.  A car can crash.  A car can start the
# engine and make a sound.  The car can also turn or rotate.

# Change (NEW COPY)
# name_of_node = current_node
# print("You moved...")
# print(" ")


# def move(self, direction):
#    global current_node
#    current_node = globals()[getattr(self, direction)]

# except KeyError:
# print("You cannot go this way.")
