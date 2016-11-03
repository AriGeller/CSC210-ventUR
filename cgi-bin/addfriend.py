#!/usr/bin/env python

import sqlite3
import cgi

form = cgi.FieldStorage()

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = form['username'].value
friend = form['friend'].value
status = #accepted, pending, requested

c.execute('INSERT INTO ?_friends VALUES (?, ?)', (username, friend, status))