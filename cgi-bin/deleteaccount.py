#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import json
import sqlite3

form = cgi.FieldStorage()

print 'Content-Type: application/json\n\n'

user = form['Username'].value

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('DELETE FROM users WHERE username = ?', [user])

conn.commit()
conn.close()

data = {}
print json.dumps(data)
