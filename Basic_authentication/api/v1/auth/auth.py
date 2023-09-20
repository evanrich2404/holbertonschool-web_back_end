#!/usr/bin/env python3
"""Module for Auth class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method for validating if the path requires authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

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
