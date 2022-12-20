from flask import Flask
from random import randint


app = Flask(__name__)


guess = randint(0,9)

@app.route("/")
def index():
    return "<h1>Guess the number!</h1>"\
         "<img src=https://media0.giphy.com/media/11BEQyXROgnLTG/200.webp?cid=bb5a1c3aa3d9hg2hv7jroidb6krgtxom9e31fb5yqtqv8ppz&rid=200.webp&ct=g>"

@app.route("/<int:number>")
def numb(number):
    if number == guess:
        return "<h1 style='color: green'>You found me!</h1>"\
            "<img src=https://media3.giphy.com/media/nVVVMObc3KyrMfGw1z/200w.webp?cid=bb5a1c3aa3d9hg2hv7jroidb6krgtxom9e31fb5yqtqv8ppz&rid=200w.webp&ct=g>"
    elif number > guess:
        return "<h1 style='color: purple'>Too high, try again!</h1>"\
            "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    else:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
            "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
app.run(debug=True)
