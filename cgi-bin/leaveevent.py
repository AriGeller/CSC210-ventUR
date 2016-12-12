#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import json
import sqlite3

print 'Content-Type: application/json\n\n'

form = cgi.FieldStorage()

user = form['username'].value
eventid = form['eventid'].value

conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('SELECT guests FROM events WHERE eventid = ?', [eventid])

guests = eval(c.fetchone()[0])

if user in guests:
    guests.remove(user)

c.execute('UPDATE events SET guests = ? WHERE eventid = ?', (repr(guests), eventid))

conn.commit()
conn.close()

data = {}
print json.dumps(data)
