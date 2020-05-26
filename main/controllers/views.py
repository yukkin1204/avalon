import flask
from main import app
from main.models.entry import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.all()
    return flask.render_template('entries.html', entries=entries)

