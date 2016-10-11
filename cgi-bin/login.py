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

#TODO 'Remember me' checkbox, captcha after n failed login attempts, locking accounts after m failed attempts, time delay between login attempts

c.execute('SELECT salt FROM users WHERE username = ?', (username,))
salt = c.fetchone()[0]

dk = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password, salt, 512000))
c.execute('SELECT password FROM users WHERE username = ?', (username,))
dk2 = c.fetchone()[0]

if(dk == dk2):
