#!/usr/bin/env python
# coding=utf-8
from flask_app import app


if __name__ == '__main__':
    app.debug = True
    app.run()
