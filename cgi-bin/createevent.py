#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3

form = cgi.FieldStorage()

name = form['EventName'].value
owner = form['Username'].value
start = form['StartTime'].value
end = form['EndTime'].value
location = form['Location'].value
description = form['Description'].value
privacy = form['Privacy'].value # Don't worry about this yet

conn = sqlite3.connect('events.db')
c = conn.cursor()

# need to create unique eventid

c.execute('INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (eventid, name, owner, start, end, location, description, privacy))

conn.commit()
conn.close()
