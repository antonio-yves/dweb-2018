# -*- coding: utf-8 -*-

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filmes')
def filmes():
    return render_template('filmes/index.html')
