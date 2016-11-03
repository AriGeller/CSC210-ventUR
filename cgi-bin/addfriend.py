#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import sqlite3
import cgi

form = cgi.FieldStorage()

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = form['username'].value
friend = form['friend'].value

c.execute('SELECT status FROM ?_friends WHERE username = ?', (username, friend))
status = c.fetchone()[0]


if status is None:
    c.execute('INSERT INTO ?_friends VALUES (?, ?)', (username, friend, "pending"))
    c.execute('INSERT INTO ?_friends VALUES (?, ?)', (friend, username, "requested"))
elif status == "requested":
    c.execute('UPDATE ?_friends SET status = "accepted" WHERE username = ?', (friend, username))
    c.execute('UPDATE ?_friends SET status = "accepted" WHERE username = ?', (username, friend))
