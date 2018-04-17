import random
"""

This is a guide of how to make
hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. Hide and reveal letters
5. Create win and lost conditions

"""

print(" ")
print("Hello, and welcome to HANGMAN.")
print("You have 10 guesses to win, good luck.")

word_bank = ["Maroon", "Cyan", "Turquoise", "Sage", "Light Orange",
             "Light Pink", "Dark Indigo", "Bright Red", "Ultramarine Blue", "Bright Pink"]
guesses_number = 10
subtracted = 1
random_word = random.choice(word_bank)
list(random_word)
letters_guessed = []

while True:
    # Print out the *s
    output = []
    for letter in random_word:
        if letter.lower() in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))

    if output == list(random_word):
        print(" ")
        print("You figured out the word!")
        exit(0)

    # Ask for input
    print(" ")
    guess = input("I guessed... ").lower()
    print(" ")
    letters_guessed.append(guess)
    print(letters_guessed)

    if guess not in random_word.lower():
        print(" ")
        guesses_number = guesses_number - subtracted
        print("That is not a letter of the word.")
        print("You have %s guesses left." % guesses_number)

    print(" ")

    if guesses_number == 0:
        exit()
