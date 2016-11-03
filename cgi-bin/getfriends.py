#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import sqlite3
import json
import cgi

form = cgi.FieldStorage()

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = form['username'].value
status = "accepted"

c.execute('SELECT friends FROM ?_friends WHERE status = ?', (username, status))

friends = c.fetch()

print json.dumps(friends)
