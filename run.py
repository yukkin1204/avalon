from main import app
from main.controllers import user_controller \
                            , game_controller \
                            , game_ready_controller

if __name__ == '__main__':
    app.run(debug=True)


