#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301


import cgi
import cgitb
import sqlite3
import json

cgitb.enable()

form = cgi.FieldStorage()



print 'Content-Type: application/json\n\n'

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = form['username'].value
friend = form['friend'].value

data = {}

insert = 'INSERT INTO %s_friends VALUES (?, ?)' % username
c.execute(insert, (friend, "accepted"))
conn.commit()
conn.close()

print json.dumps(data)
