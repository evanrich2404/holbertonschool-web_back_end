#!/usr/bin/env python3
"""Module for Auth class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method for validating if the path requires authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method for validating if the header contains the Authorization
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method for getting the current user
        """
        return None
