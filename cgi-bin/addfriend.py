#!/usr/bin/env python

import sqlite3
import cgi

form = cgi.FieldStorage()

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = form['username'].value
friend = form['friend'].value

c.execute('SELECT status FROM ?_friends WHERE username = ?' (username, friend))
status = c.fetchone()[0]

if(status == "pending"):
	
else if(status == "requested"):

else:
	c.execute('INSERT INTO ?_friends VALUES (?, ?)', (username, friend, "requested"))
	c.execute('INSERT INTO ?_friends VALUES (?, ?)', (friend, username, "pending"))