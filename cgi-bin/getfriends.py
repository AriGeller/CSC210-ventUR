#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

status = "accepted"

c.execute('SELECT friends FROM ?_friends WHERE status = ?', (username, status))

friends = c.fetch()

#return friends as json