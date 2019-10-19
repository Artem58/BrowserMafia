from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', serverTime=str(datetime.now()).split('.')[0])


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


@app.route('/chooseGame')
def chooseGame():
    return render_template('chooseGame.html')


@app.route('/createGame')
def createGame():
    return render_template('createGame.html')


@app.route('/game')
def game():
    return render_template('game.html')


if __name__ == "__main__":
    app.run("127.0.0.1", 80)
