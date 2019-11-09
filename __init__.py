from datetime import datetime
from json import dumps
from json import loads
from random import randint

from flask import Flask
from flask import abort
from flask import redirect
from flask import render_template
from flask import request

app = Flask(__name__)

userDB = {
    'admin': 'admin',
    'hero': '135c',
    'underwoe': '1235v'
}

tokenDB = []


@app.route('/')
def index():
    return render_template('index.html', serverTime=str(datetime.now()).split('.')[0])


@app.route('/signUp', methods=['GET'])
def signUp():
    return render_template('signUp.html')


@app.route('/signUp', methods=['POST'])
def register():
    userData = loads(request.data)
    if userData['user'] in userDB:
        abort(404)
    userDB[userData['user']] = userData['password']
    return redirect('/')


@app.route('/chooseGame')
def chooseGame():
    if request.cookies['token'] in tokenDB:
        return render_template('chooseGame.html')
    else:
        abort(404)


@app.route('/createGame')
def createGame():
    if request.cookies['token'] in tokenDB:
        return render_template('createGame.html')
    else:
        abort(404)


@app.route('/game')
def game():
    if request.cookies['token'] in tokenDB:
        return render_template('game.html')
    else:
        abort(404)


@app.route('/verifyUser', methods=['POST'])
def verifyUser():
    userData = loads(request.data)
    if userData['user'] in userDB and userDB[userData['user']] == userData['password']:
        t = str(randint(0, 1023))
        tokenDB.append(t)
        return dumps({"token": t})
    else:
        abort(404)


if __name__ == "__main__":
    app.run("127.0.0.1", 80)
