#!/usr/bin/env python

# pylint: disable=0103
# pylint: disable=0301


import cgi
import cgitb
import sqlite3
import json

cgitb.enable()

form = cgi.FieldStorage()



print 'Content-Type: application/json\n\n'

conn = sqlite3.connect('users.db')
c = conn.cursor()
conn.text_factory = str

username = form['username'].value
friend = form['friend'].value



data = {}

try: 	
	insert = 'INSERT INTO %s_friends VALUES (?, ?)' % username
	c.execute(insert, (friend, "accepted"))
	conn.commit()
	conn.close()
except:
	oops = "oops"



print json.dumps(data)
    

