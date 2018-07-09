# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, render_template

from app import app

lista_filmes = ['Star Wars', 'Toy Story', 'Taxi Driver']

@app.route('/')
def index():
    return render_template('index.html')

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