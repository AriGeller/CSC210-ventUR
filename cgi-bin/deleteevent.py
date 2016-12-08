#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import json
import sqlite3

form = cgi.FieldStorage()

print 'Content-Type: application/json\n\n'

eventid = form['EventID'].value

conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('DELETE FROM events WHERE eventid = ?', [eventid])

conn.commit()
conn.close()

data = {}
print json.dumps(data)
