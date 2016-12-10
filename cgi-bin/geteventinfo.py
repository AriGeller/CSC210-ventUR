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

c.execute('SELECT * FROM events WHERE eventid = ?', [eventid])

data = {}
row = c.fetchone()
data['ID'] = row[0]
data['name'] = row[1]
data['owner'] = row[2]
data['startime'] = row[3]
data['endtime'] = row[4]
data['location'] = row[5]
data['description'] = row[6]
data['guests'] = eval(row[7]) # python list of guests attending event, may return an empty list

print json.dumps(data)
