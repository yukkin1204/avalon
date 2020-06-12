import flask
from flask import render_template
from main import app
from main.models.game import Game

@app.route('/games', methods=['POST'])
def create_game():
    game = Game()
    

