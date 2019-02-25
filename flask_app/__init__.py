#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:abc123@localhost:3306/envmondb48'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
db = SQLAlchemy(app)

from flask_app import views
