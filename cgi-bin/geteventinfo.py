#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3
import json

print 'Content-Type: application/json\n\n'

form = cgi.FieldStorage()

eventid = form['EventID'].value

conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('SELECT name, owner, starttime, endtime, location, description FROM events WHERE eventid = ?', [eventid])

data = {}
row = c.fetchone()
data['name'] = row[0]
data['owner'] = row[1]
data['startime'] = row[2]
data['endtime'] = row[3]
data['location'] = row[4]
data['description'] = row[5]
data['guests'] = eval(row[6]) # python list of guests attending event, may return an empty list

print json.dumps(data)
