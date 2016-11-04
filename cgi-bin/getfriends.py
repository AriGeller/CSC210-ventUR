#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import sqlite3
import json
import cgi

form = cgi.FieldStorage()

print "Content-Type: application/json\n\n"

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = form['username'].value
status1 = "accepted"
status2 = "pending"

getFriends = "SELECT friends FROM %s_friends" % username

c.execute(getFriends)

friends = c.fetchall()




data = {}
data['friends'] = friends


print json.dumps(data)
