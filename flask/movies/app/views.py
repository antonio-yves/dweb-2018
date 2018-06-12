# -*- coding: utf-8 -*-

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filmes')
def filmes():
    lista_filmes = ['Star Wars', 'Toy Story', 'Taxi Driver']
    return render_template(
        'filmes/index.html',
        filmes=lista_filmes
    )
