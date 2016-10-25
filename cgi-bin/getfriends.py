#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('SELECT friends FROM %s_friends', username)

friends = c.fetch()

for friend in friends:
	print friend