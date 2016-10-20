#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301


import binascii
import cgi
import cgitb
import hashlib
import json
import sqlite3

print "Content-Type: application/json"
print

cgitb.enable()

f = open("test.txt", "w")
f.write("test")

form = cgi.FieldStorage()
f.write("storage")

username = form['Username'].value
f.write("username")
password = form['Password'].value
f.write("password")

conn = sqlite3.connect('users.db')
f.write("connect")
c = conn.cursor()
f.write("cursor")
conn.text_factory = str

f.write("factory")

data = {}

c.execute('SELECT salt FROM users WHERE username = ?', [username])

f.write("select salt")
# Fetch salt from database
salt = c.fetchone()[0]

f.write("fetchone salt")

# Computer hash using salt and provided password
dk = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password, salt, 512000))

f.write("dk")
# Fetch password hash from database
c.execute('SELECT password FROM users WHERE username = ?', [username])

f.write("get password")
dk2 = c.fetchone()[0]
f.write("dk2")

f.close()
# Compare database hash to computed hash
if dk == dk2:
    data["test"] = "pass"
    print json.dumps(data)
    # end
