#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import sqlite3
import json
import cgitb


print "Content-Type: text/plain\n"


cgitb.enable()
form = cgi.FieldStorage()
userTest = form['Username'].value
	
conn = sqlite3.connect('users.db')
c = conn.cursor()

data = {}

for user in c.execute("SELECT * FROM users WHERE username =?", [userTest]):
	data['name'] = "name"
	    



