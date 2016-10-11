#!/bin/bash/python

import cgi
import sqlite3

form = cgi.FieldStorage()
checkuser = form['Username'].value

data = {}

conn = sqlite3.connect('users.db')
c = conn.cursor()

dbuser = c.execute('SELECT ')