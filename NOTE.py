'''

import string
# Guessing game (TIP)
# Initializing variables

# LOOP: Describe ONE turn (This is the game's controller)

# End game in while loop

# Lists

the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ["cheese", "meat", "sauce", "sesame seed bun", "avocado", "onion"]
print(cheeseburger_ingredients[0])
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))

# Going through lists
for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for item in the_count:
    print(item)

# Multiply by 2

for num in the_count:
    print(num * 2)

length = len(cheeseburger_ingredients)
range(5)  # A List of the  numbers 0 through 4
range(len(cheeseburger_ingredients))  # Generates a list of all indices

for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s." % (num, item))

# Recasting into a list
strOne = "Hello World!"
listOne = list(strOne)
print(listOne)
listOne[11] = "."  # Changes "!" into a "."
print(listOne)

# Adding things to a list
cheeseburger_ingredients.append("fries")
print(cheeseburger_ingredients)
cheeseburger_ingredients.append("lettuce")
print(cheeseburger_ingredients)

# Remove things from a list
cheeseburger_ingredients.pop(1)
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("cheese")
print(cheeseburger_ingredients)

# Getting the alphabet

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

# Making things lowercase
strTwo = "ThIs Is A VeRY ODd sEnTeNCe"
lowercase = strTwo.lower()
print(lowercase)

'''

# output = [], guesses_left = 10, letters_guessed = ['z', 'd',]

# Dictionaries - Made up of key: value pair

dictionary = {"name": "Short", "age": 14, "height": 6 * 12 + 2}  # Do not put comma at end of last item " , "

# Accessing things from a dictionary
print(dictionary["name"])
print(dictionary["age"])
print(dictionary["height"])

# Add a pair to dictionary
dictionary["Profession"] = "telemarketer"

large_dictionary = {
    "CA": "California",
    "AZ": "ARIZONA",
    "NY": "NEW YORK"
}
print(large_dictionary["NY"])

larger_dictionary = {
    "CA": [
        "Fresno",
        "San Francisco",
        "San Jose"
    ],
    "AZ": [
        "Phoenix",
        "Tuscon"
    ],
    "NY": [
        "Brooklyn",
        "New York City"
    ]
}
print(larger_dictionary["NY"])  # Gives a list
print(larger_dictionary["NY"][1])  # Gives one
print(larger_dictionary["AZ"][0])

#  Nested dictionary
largest_dictionary = {
    "CA": {
        "Name": "California",
        "Population": 39250000,
        "Border ST": [
            "Oregon",
            "Nevada",
            "Arizona"

        ]
    },
    "AZ": {
        "Name": "Arizona",
        "Population": 6931000,
        "Border ST": [
            "California",
            "Utah",
            "Nevada",
            "New Mexico"
        ]
    },
    "NY": {
        "Name": "New York",
        "Population": 19750000,
        "Border ST": [
            "Vermont",
            "Massachusetts",
            "Connecticut",
            "Pennsylvania",
            "New Jersey"
        ]
    }
}

current_node = largest_dictionary["NY"]
print(current_node["Name"])
print(current_node["Population"])













