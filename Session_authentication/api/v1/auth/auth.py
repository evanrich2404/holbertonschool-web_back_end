#!/usr/bin/env python3
"""Module for Auth class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method for validating if the path requires authentication"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Method for validating if the header contains the Authorization
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method for getting the current user
        """
        return None

    def session_cookie(self, request=None):
        """
        Method for getting a cookie value from a request
        """
        if request is None:
            return None

        _my_session_id = getenv('SESSION_NAME')

        return request.cookies.get(_my_session_id)
