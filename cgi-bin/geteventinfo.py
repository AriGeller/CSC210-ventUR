#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3

form = cgi.FieldStorage()

eventid = form['EventID'].value

conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('SELECT * FROM events WHERE eventid = ?', [eventid])

data = {}
#need to properly format data
#data['name'] = c.fetch...?

print json.dumps(data)
