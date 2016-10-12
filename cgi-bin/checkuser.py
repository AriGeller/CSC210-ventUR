#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3
import json
import cgitb


print "Content-Type: application/json"
print



cgitb.enable()

form = cgi.FieldStorage()

userTest = form['username'].value

conn = sqlite3.connect('users.db')

c = conn.cursor()


data = {}

for user in c.execute("SELECT * FROM users WHERE username =?", [userTest]):
        data['name'] = user[0]
        data['test'] = user[3]


print json.dumps(data)

