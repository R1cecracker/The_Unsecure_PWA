# this module handles the secure functions for the app

import bcrypt


def getSalt():
    salt = bcrypt.gensalt()
    return salt


def hash(password, salt):
    bytes = password.encode("utf-8")
    hashpw = bcrypt.hashpw(bytes, salt)
    return hashpw


# Example password
