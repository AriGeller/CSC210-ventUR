#!/usr/bin/python

# pylint: disable=C0103

import cgi
import sqlite3
import json
import cgitb
import sys
import traceback


print "Content-Type: application/json\n\n"


sys.stderr = sys.stdout


try:
	cgitb.enable()

	form = cgi.FieldStorage()
	usertest = form['Username'].value

	conn = sqlite3.connect('users.db')
	c = conn.cursor()

	data = {}

	for user in c.execute("SELECT * FROM users WHERE username = ?", [userTest]):
	    data['name'] = user[0]
	    

	print json.dumps(data)
except:
	print "\n\n<PRE>"
	traceback.print_exec()

