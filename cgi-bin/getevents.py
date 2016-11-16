#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3

form = cgi.FieldStorage()

owner = form['Username'].value

conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('SELECT eventid FROM events WHERE owner = ?', [owner])

data = {}
data['events'] = c.fetchall()

print json.dumps(data)
