#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import cgitb
import binascii
import hashlib
import json
import sqlite3

print "Content-type: application/json\n\n"

cgitb.enable()

f = open("test.txt", "w")


form = cgi.FieldStorage()


username = form['Username'].value

attempt = form['Password'].value


f.write("Password = " + attempt + "\n")

conn = sqlite3.connect('users.db')

c = conn.cursor()

conn.text_factory = str



data = {}

c.execute('SELECT salt FROM users WHERE username = ?', [username])

# Fetch salt from database
salt = c.fetchone()[0]
f.write("Salt =  " + salt + "                         ")

# Computer hash using salt and provided password
dk = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', attempt, salt, 512000))

# Fetch password hash from database
c.execute('SELECT password FROM users WHERE username = ?', [username])

dk2 = c.fetchone()[0]

f.write(dk + "    ")
f.write(dk2 + "   ")


f.close()
# Compare database hash to computed hash
if dk == dk2:
    data["test"] = "pass"
    print json.dumps(data)
    # end
