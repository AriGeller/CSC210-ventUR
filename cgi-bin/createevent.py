#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3
from random import randint
import json

form = cgi.FieldStorage()

print 'Content-Type: application/json\n\n'

name = form['EventName'].value
owner = form['Username'].value
start = form['StartTime'].value
end = form['EndTime'].value
location = form['Location'].value
description = form['Description'].value
guests = None #Don't worry about this yet
#privacy = form['Privacy'].value # Don't worry about this yet either

conn = sqlite3.connect('events.db')
c = conn.cursor()

#This is hacky but I think it works
eventid = randint(0, 99999999)
while True:
	c.execute('SELECT name FROM events WHERE eventid = ?', [eventid])
	if c.fetchone() is None:
	    break
	else:
	    eventid = randint(0, 99999999)

c.execute('INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (eventid, name, owner, start, end, location, description, guests))

conn.commit()
conn.close()

data = {}

print json.dumps(data)
