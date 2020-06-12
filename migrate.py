from main import app
from main.models import db
from flask_migrate import Migrate
from main.models.user import *
from main.models.game import *
from main.models.game_element import *

migrate = Migrate(app, db)

