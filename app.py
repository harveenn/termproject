from flask import Flask, render_template, request
import random

app = Flask(__name__)

movies = ["die hard", "the dark knight", "black widow", "hocus pocus", "star wars", "home alone", "forest gump", "the sixth sense", "amelie", "spiderman", "pirates of the caribbean", "the exorcist", "get out", "black panther", "cabaret", "the great gatsby", "crazy rich asians", "the notebook", "wedding creahsers", "twilight"]

max_incorrect_guesses = 6 

hangman_message = ["You have six guesses left", "You have five guesses left", "You have four guesses left", "You have three guesses left", "You have two guesses left", "You have one guess left", "HANGMAN!"]
hangman_images = ["static/h1.PNG", "static/h2.PNG", "static/h3.PNG", "static/h4.PNG", "static/h5.PNG", "static/h6.PNG", "static/h7.PNG"]

def get_displayed_movies(movie, guessed_letters, num_incorrect_guesses):
    if num_incorrect_guesses == max_incorrect_guesses:
        return "You loose! The movie was: " + movie.upper(), "static/h7.PNG", ""
    elif all(letter in guessed_letters for letter in movie if letter != " "):
        return "You win!", " ", " "
    else:
        message = hangman_message[num_incorrect_guesses]
        image = hangman_images[max_incorrect_guesses - num_incorrect_guesses - 1]
        displayed_movie = get_displayed_movies(movie, guessed_letters)
        return message, image, displayed_movie

def play_game(movie, guessed_letters, num_incorrect_letters):
    displayed_movie = ""
    for letter in movie:
        if letter == " ":
            displayed_movie += " "
        elif letter in guessed_letters:
            displayed_movie += letter.upper() + " "
        else:
            displayed_movie += "_"
    return displayed_movie.strip()
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        movie = random.choice(movies)
        guessed_letters = []
        num_incorrect_guesses = 0 
        message, image, displayed_movie = play_game(movie, guessed_letters, num_incorrect_guesses)
        return render_template("index.html", message=message, image=image, displayed_movie=displayed_movie)
    elif request.method == "POST":
        guess = request.form["guess"].lower()
        movie = request.form["movie"].lower()
        guessed_letters = request.form.getlist("guessed_letters[]")
        num_incorrect_guesses = int(request.form["num_incorrect_guesses"])
        guessed_letters.append(guess)
        if guess not in movie:
            num_incorrect_guesses += 1
            message, image, displayed_movie = play_game(movie, guessed_letters, num_incorrect_guesses)
            return render_template("index.html", message=message, image=image, displayed_movie=displayed_movie, guess=guess, movie=movie, guessed_letters=guessed_letters, num_incorrect_guesses=num_incorrect_guesses)
        
if __name__ == "__main__":
    app.run(debug=True)