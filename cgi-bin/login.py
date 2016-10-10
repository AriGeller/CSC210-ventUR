#!/usr/bin/python

import sqlite3
import binascii, hashlib, os

salt = os.urandom()
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 512000)
binascii.hexlify(dk)