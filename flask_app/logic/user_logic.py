#!/usr/bin/env python
# coding=utf-8
from flask_app.models.models import Userinfo


class UserLogic:
    def __init__(self):
        pass

    @staticmethod
    def get_user_name(username=None):
        if username is None:
            return None
        else:
            user = Userinfo.query.filter(Userinfo.username == username).first()
            if user is not None:
                return user
            else:
                return None
