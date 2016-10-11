#!/usr/bin/python
# pylint: disable=C0103
# pylint: disable=C0301

import sqlite3
import cgi
import binascii
import hashlib
import os
from base64 import b64encode

form = cgi.FieldStorage()

username = form['Username'].value
firstname = form['FirstName'].value
lastname = form['LastName'].value
email = form['email'].value
password = form['Password'].value

# TODO check for common/insecure passwords

conn = sqlite3.connect('users.db')
c = conn.cursor()
conn.text_factory = str

salt = os.urandom(64)
salt = b64encode(salt).decode('utf-8')

dk = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password, salt, 512000))

c.execute('INSERT INTO users VALUES (?,?,?,?,?,?)', (username, email, dk, firstname, lastname, salt))

conn.commit()
conn.close()
