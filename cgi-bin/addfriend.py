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

sql = "SHOW TABLES LIKE %s_friends" % username
c.execute(sql)
result = c.fetchone()[0]
if result:
	sql = "INSERT INTO %s_friends VALUES (?, ?)" % username
    c.execute(sql, (friend, "pending"))
    sql = "INSERT INTO %s_friends VALUES (?, ?)" % friend
    c.execute(sql, (username, "requested"))
else:
	sql = "SELECT status FROM %s_friends WHERE username = ?" % username
	c.execute(sql, [friend])
	status = c.fetchone()[0]
	sql = "UPDATE %s_friends SET status = accepted WHERE username = ?" % friend
    c.execute(sql, [username])
    sql = "UPDATE %s_friends SET status = accepted WHERE username = ?" % username
    c.execute(sql, [friend])