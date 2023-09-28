#!/usr/bin/env python3
"""Auth Module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Method that takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
