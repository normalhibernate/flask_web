#!/usr/bin/env python
# coding=utf-8
from flask_app import db


class DbHelper:
    def __init__(self):
        pass

    def select(self, sql, *value):
        sql_str = sql.formatter()
        data_query = db.session.execute(sql_str)
        print data_query
        for user in data_query:
            print user.username
        pass


if __name__ == '__main__':
    values = ["admin", '2']
    dicts = {"username": "admin", "username2": '2'}
    sql = "select username,password from userinfo where username = '{0[0]}' or username ='{0[1]}'"
    sql2 = "select username,password from userinfo where username = '{username}' or username ='{username2}'"
    print sql.format(values)
    print sql2.format(**dicts)
    data_query = db.session.execute(sql.format("admin", 1))
    for user in data_query:
        print user.username