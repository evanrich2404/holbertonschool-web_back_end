#!/usr/bin/env python3
"""Auth Module"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB


def _hash_password(password: str) -> bytes:
    """Method that takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    from user import User

    def register_user(self, email: str, password: str) -> User:
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hash_password = _hash_password(password)
            user = self._db.add_user(email, hash_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False
