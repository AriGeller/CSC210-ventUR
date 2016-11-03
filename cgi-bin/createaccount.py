3#!/usr/bin/env python

# pylint: disable=C0103
# pylint: disable=C0301

import cgi
import cgitb
import sqlite3
import binascii
import hashlib
import os
from base64 import b64encode

cgitb.enable()

form = cgi.FieldStorage()

print 'Content-Type: text/html\n\n'


username = form['Username'].value

firstname = form['FirstName'].value
lastname = form['LastName'].value
email = form['email'].value
password = form['Password'].value


conn = sqlite3.connect('users.db')
c = conn.cursor()
conn.text_factory = str

# Generate random string
salt = os.urandom(64)
salt = b64encode(salt).decode('utf-8')

# Compute hash using password and salt
dk = hashlib.sha256(password + salt).hexdigest()

# Insert values into database
c.execute('INSERT INTO users VALUES (?,?,?,?,?,?)', (username, email, dk, firstname, lastname, salt))

c.execute('CREATE TABLE ?_friends(username varchar(100) primary key, status varchar(10))', username)

conn.commit()
conn.close()

redirectURL = "../FirstLogin-Page.html"




print 'Location: %s' % redirectURL
print # HTTP says you have to have a blank line between headers and content
print '<html>'
print '  <head>'
print '    <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print '    <title>You are going to be redirected</title>'
print '  </head>'
print '  <body>'
print '    Redirecting... <a href="%s">Click here if you are not redirected</a>' % redirectURL
print '  </body>'
print '</html>'
