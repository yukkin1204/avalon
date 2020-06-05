import flask
from flask import render_template
from main import app
from main.models.game import Game

@app.route('/games', methods=['GET'])
def show_game_list():
    games = Game.list()
    return render_template('games/index.html', title='Game List', games=games)

