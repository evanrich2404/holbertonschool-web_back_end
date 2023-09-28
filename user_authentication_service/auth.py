#!/usr/bin/env python3
"""Auth Module.

This module provides authentication and session management functionalities.
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.

    Provides methods for user registration, login validation,
    session management, password reset functionality, and more.
    """

    def __init__(self):
        self._db = DB()

    from user import User

    def register_user(self, email: str, password: str) -> User:
        """Register a new user.

        Args:
            email (str): User's email.
            password (str): User's password.

        Raises:
            ValueError: If the user already exists.

        Returns:
            User: The newly registered user.
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hash_password = _hash_password(password)
            user = self._db.add_user(email, hash_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user's login credentials.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for a user.

        Args:
            email (str): User's email.

        Returns:
            str: The new session ID.
        """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()

        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User or None:
        """Retrieve a user based on their session ID.

        Args:
            session_id (str): The session ID for the user.

        Returns:
            User or None: Returns the user associated with the session ID
            or None if not found.
        """
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Terminate a user's session.

        Args:
            user_id (int): The ID of the user.

        Returns:
            None
        """
        if not user_id:
            return None

        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for the user.

        Args:
            email (str): The email of the user.

        Raises:
            ValueError: If the user with the provided email is not found.

        Returns:
            str: The reset token.
        """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound as e:
            raise ValueError from e

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using the reset token.

        Args:
            reset_token (str): The token to identify
            the user for password reset.
            password (str): The new password for the user.

        Raises:
            ValueError: If no user is associated with the provided reset token.

        Returns:
            None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hash_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hash_password,
                                 reset_token=None)
        except NoResultFound as e:
            raise ValueError from e


def _generate_uuid() -> str:
    """Generate a UUID.

    Returns:
        str: A new UUID as a string.
    """
    return str(uuid.uuid4())
