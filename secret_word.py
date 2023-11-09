## I really struggle with this program. I tried my best but I needed to use Chat GPT
## To ask for help so I tried to learn a little.

import random

# Def here is been used to create a funtion that I'll use latter in my code
def choose_word():
    words = ['mosiah']
    return random.choice(words)

def display_hint(word, guessed_letters):
    # I diplayed hint as a string in blank to asighn something after
    hint = ""
    for letter in word:
        if letter in guessed_letters:
            hint += letter + " "
        else:
            hint += "_ "
    return hint

def word_guessing_game():
    print("Welcome to the word guessing game!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    while True:
        hint = display_hint(word_to_guess, guessed_letters)
        print("Your hint is:", hint)
        guess = input("What is your guess? ").lower()

        if guess == word_to_guess:
            print("Congratulations! You guessed it!")
            print(f'It took you {attempts} guesses')
            break
        else:
            guessed_letters.extend(guess)
            attempts += 1

if __name__ == '__main__':
    word_guessing_game()