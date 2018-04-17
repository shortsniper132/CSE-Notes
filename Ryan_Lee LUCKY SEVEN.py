import random
print("This is Lucky 7's, in this game the dice will roll randomly, if you get 7, you gain $5, each time you roll, ")
print("you lose $1.  You start with $15 and 2 dice; the dices will now begin to roll.")

# I cannot find the reason for the numbers restarting after the loop.   Due to this, there's a problem.


def restart():
    return do_again()


def do_again():
    while True:
        print(" ")

        print("Rolling...")

        print(" ")

        import time
        time.sleep(5)

        r = 0
        add = 1
        if r > 0:
            addition_points = r + + add
            print(":Round %s:" % addition_points)

        print(" ")

        dice_one = (random.randint(1, 6))
        dice_two = (random.randint(1, 6))

        addition_together = dice_one + + dice_two

        print("You rolled %s for dice 1." % dice_one)
        print("You rolled %s for dice 2." % dice_two)
        print("You got %s in total." % addition_together)

        print(" ")

        num1 = 15

        if dice_one + + dice_two == 7:
            num1 += 4

        if dice_one + + dice_two != 7:
            num1 -= 1

        print("You have now have $%s." % num1)

        if num1 <= 0:
            print("You lost all of your money!")
            print("You lasted for %s round." % r)
            exit()

            return restart()


restart()

#  Cash doesn't go down or up due to loop.
