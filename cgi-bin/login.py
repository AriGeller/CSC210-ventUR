#!/usr/bin/python
# pylint: disable=C0103
# pylint: disable=C0301

import sqlite3
import cgi
import binascii
import hashlib

form = cgi.FieldStorage()

username = form['Username'].value
password = form['Password'].value

conn = sqlite3.connect('users.db')
c = conn.cursor()
conn.text_factory = str

c.execute('SELECT salt FROM users WHERE username = ?', [username])
# Fetch salt from database
salt = c.fetchone()[0]

# Computer hash using salt and provided password
dk = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password, salt, 512000))
# Fetch password hash from database
c.execute('SELECT password FROM users WHERE username = ?', [username])
dk2 = c.fetchone()[0]

# Compare database hash to computed hash
if(dk == dk2):
