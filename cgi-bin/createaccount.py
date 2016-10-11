#!/usr/bin/python
# pylint: disable=C0103
# pylint: disable=C0301

import sqlite3
import cgi
import binascii
import hashlib
import os

form = cgi.FieldStorage()

username = form['Username'].value
firstname = form['FirstName'].value
lastname = form['LastName'].value
email = form['email'].value
password = form['Password'].value

# TODO check for common/insecure passwords

conn = sqlite3.connect('users.db')
c = conn.cursor()

salt = os.urandom(128)
dk = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 512000))

c.execute('INSERT INTO users VALUES (?,?,?,?,?,?)', (username, email, dk, firstname, lastname, salt))

conn.commit()
conn.close()
