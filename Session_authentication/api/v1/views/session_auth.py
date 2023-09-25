#!/usr/bin/env python3
"""session auth route module"""
from flask import jsonify, request, make_response
from models.user import User
from os import getenv
from api.v1.views import app_views


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """setting up checks for email and password"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = make_response(user.to_json())
    SESSION_NAME = getenv('SESSION_NAME')
    response.set_cookie(SESSION_NAME, session_id)

    return response
