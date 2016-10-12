#!/bin/bash/python
# pylint: disable=C0103

import cgi
import sqlite3
import json
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
username = form['Username'].value

conn = sqlite3.connect('users.db')
c = conn.cursor()

data = {}

for user in c.execute('SELECT user FROM users WHERE username = ?', (username,)):
    data['name'] = user[0]

print json.dumps(data)
