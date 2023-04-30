import random

"""
The first step in the code is to write a list of movies that the player will guess from.
"""

movies = ["die hard", "the dark knight", "black widow", "hocus pocus", "star wars", "home alone", "forest gump", "the sixth sense", "amelie", "spiderman", "pirates of the caribbean", "the exorcist", "get out", "black panther", "cabaret", "the great gatsby", "crazy rich asians", "the notebook", "wedding creahsers", "twilight"]

movie = random.choice(movies)

guessed_letters = []
max_incorrect_guesses = 6

hangman_message = ["You have six guesses left", "You have five guesses left", "You have four guesses left", "You have three guesses left", "You have two guesses left", "You have one guess left", "HANGMAN!"]

# Display current status of hangman game
def display_hangman(num_incorrect_guesses):
    print(hangman_message[num_incorrect_guesses])

# Current status of words with underscore for unguessed letters
def display_movie(movie, guessed_letters):
    for letter in movie:
        if letter == " ":
            print(" ", end=" ")
        elif letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

# playing the game 
num_incorrect_guesses = 0 
while num_incorrect_guesses < max_incorrect_guesses:
    display_hangman(num_incorrect_guesses)
    display_movie(movie, guessed_letters)
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters: 
        print("You already guessed this letter.")
    elif guess in movie:
        print("Correct!")
        guessed_letters.append(guess)
        if all(letter in guessed_letters for letter in movie if letter != " "):
            print("You win!")
            break
    else:
        print("Incorrect.")
        num_incorrect_guesses += 1
        guessed_letters.append(guess)

display_hangman(num_incorrect_guesses)
if num_incorrect_guesses == max_incorrect_guesses:
    print("You loose! The movie was:", movie)

