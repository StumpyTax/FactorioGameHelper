from os import curdir
from flask import Flask, render_template, request, redirect, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("items.db")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/recipes', methods=['GET'])
def recipes():
    cur = get_db().cursor()
    items = cur.execute('Select * from items').fetchall()
    return render_template('recipes.html', items=items)


@app.route('/scheme', methods=['GET'])
def scheme():
    cur=get_db().cursor()
    items=cur.execute('Select * from schemes').fetchall()
    return render_template('scheme.html',items=items)


@app.route('/guide', methods=['GET'])
def guide():
    return render_template('guide.html')


@app.route('/SpeedrunGuide', methods=['GET'])
def SpeedrunGuide():
    cur=get_db().cursor()
    items=cur.execute('Select * from speedrun').fetchall()
    return render_template('SpeedrunGuide.html',items=items)

@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run()
