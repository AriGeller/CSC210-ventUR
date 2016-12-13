#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import json
import sqlite3

form = cgi.FieldStorage()

print 'Content-Type: application/json\n\n'

user = form['Username'].value

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('DELETE FROM users WHERE username = ?', [user])
select = 'SELECT username FROM %s_friends' % user
c.execute(select)
friends = c.fetchall()
for friend in friends:
    delete = 'DELETE FROM %s_friends WHERE username = ?' % friend[0]
    c.execute(delete, [user])
friends = 'DROP TABLE %s_friends' % user
c.execute(friends)

conn.commit()
conn.close()

conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('DELETE FROM events WHERE owner = ?', [user])

conn.commit()
conn.close()

data = {}
print json.dumps(data)
