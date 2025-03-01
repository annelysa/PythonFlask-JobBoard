from flask import Flask, render_template, g
from sqlite3 import *
PATH="db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)

    if connection == None:
        connection, g._connection = sqlite3.connect(PATH)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


