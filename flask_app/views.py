#!/usr/bin/env python
# coding=utf-8
from flask import render_template

from flask_app import app
from flask_app import db
from flask_app.logic.user_logic import UserLogic


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    user = UserLogic.get_user_name(name)

    if user is not None:
        return render_template('index.html', name=name)
    else:
        return render_template('404.html', name=name)


@app.route('/maps')
def maps():
    return render_template('map.html')


@app.route('/maps2')
def maps2():
    return render_template('map2.html')
