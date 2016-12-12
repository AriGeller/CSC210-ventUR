#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3
import json

form = cgi.FieldStorage()

print 'Content-Type: application/json\n\n'


name = form['EventName'].value
owner = form['Username'].value
start = form['StartTime'].value
end = form['EndTime'].value
location = form['Location'].value
description = form['Description'].value
guests.append(owner)
guests = []
#privacy = form['Privacy'].value # Don't worry about this yet either


conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('INSERT INTO events (name, owner, starttime, endtime, location, description, guests) VALUES (?, ?, ?, ?, ?, ?, ?)', (name, owner, start, end, location, description, repr(guests)))

conn.commit()
conn.close()

data = {}

print json.dumps(data)
