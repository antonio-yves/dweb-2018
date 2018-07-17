# -*- coding: utf-8 -*-

import psycopg2, psycopg2.extras

from flask import g, session, request, redirect, url_for, render_template

from app import app

lista_filmes = ['Star Wars', 'Toy Story', 'Taxi Driver']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Connect database
# g = http://flask.pocoo.org/docs/1.0/api/#flask.g
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.before_request
def before_request():
   g.db = psycopg2.connect("dbname=movies user=guga password=gugasv host=127.0.0.1")

# Disconnect database
@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM genero;")
    data = cur.fetchall()
    cur.close()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if request.method == 'POST':
        session['name'] = request.form['nome']

    if 'name' in session:
        name = session['name']
    else:
        name = None

    return render_template('index.html', generos=data, username=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.form['user'] == 'gustavo':
            return render_template('login.html', error='usuario nao existe')
        else:
            print( request.form['user'], request.form['password'] )
            return redirect(url_for('filmes'))

@app.route('/filmes', methods=['GET', 'POST'])
def filmes():
    if request.method == 'POST':
        lista_filmes.append( request.form['filme'] )
    return render_template(
        'filmes/index.html',
        filmes=lista_filmes
    )

@app.route('/filme/<int:index>')
def filme(index):
    return render_template(
        'filmes/view.html',
        filme=lista_filmes[index]
    )