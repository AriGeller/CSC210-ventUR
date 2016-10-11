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

#TODO 'Remember me' checkbox

salt = c.execute('SELECT salt FROM users WHERE username = ?', username)

dk = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 512000))
dk2 = c.execute('SELECT password FROM users WHERE username = ?', username)

if(dk == dk2):
