#!/bin/bash/python

import cgi
import sqlite3

form = cgi.FieldStorage()
username = form['Username'].value

conn = sqlite3.connect('users.db')
c = conn.cursor()

dbuser = c.execute('SELECT user FROM users WHERE username = ?', (username,))
