#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3
import json

print 'Content-Type: application/json\n\n'

form = cgi.FieldStorage()

user = form['Username'].value

conn = sqlite3.connect('users.db')
c = conn.cursor()

sql = "SELECT username FROM {0}_friends WHERE status = 'accepted'".format(user)
c.execute(sql)

friends = c.fetchall()

conn.close()
conn = sqlite3.connect('events.db')
c = conn.cursor()

events = []

for friend in friends:
	c.execute("SELECT eventid FROM events WHERE owner = ?", [friend[0]])
	friendevents = c.fetchall()
	for event in friendevents:
		events.append(event[0])

conn.close()
data = {}
data['events'] = events
print json.dumps(data)
