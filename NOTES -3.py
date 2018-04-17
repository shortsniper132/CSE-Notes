# Defining functions
def hello_world():
    print("Hello World")


hello_world()  # Parenthesis = function not variable


def square_it(number):
    return number**2


print(square_it(3))


def bill_plus_tip_calculator(bill):  # 100 + 18%
    tax_amt = bill * 0.18
    total_bill = bill + tax_amt
    return total_bill


print("Your bill is $%d." % bill_plus_tip_calculator(100))


def distance_calc(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5
    return answer


print("Your answer is %d." % distance_calc(0, 0, 3, 4))


def pythagorean(a, b):
    inside = (a + b)
    answer = inside ** 2
    return answer


print(pythagorean(1, 2))
