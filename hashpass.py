import hashlib


def hashPass(password):

    hashed = hashlib.md5(password.encode())

    return hashed