from flask import Flask
from random import randint

random_num = randint(0, 9)
print(random_num)

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 to 9</h1>" \
           "<img src=https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp>"


@app.route("/<int:guess>")
def random_int(guess):
    if guess > random_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://a.im9.eu/wtf-he-went-a-bit-too-high.gif'/>"

    elif guess < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://assets-global.website-files.com/60740020d222cb8d835a05fc/63ce6c65bd6cc649d95e22cb_image4.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://michelleleighwrites.files.wordpress.com/2018/10/source1.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
