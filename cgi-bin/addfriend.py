#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = #username
friend = #friend username
status = #accepted, rejected, requested

c.execute('INSERT INTO ?_friends VALUES (?, ?)', (username, friend, status))