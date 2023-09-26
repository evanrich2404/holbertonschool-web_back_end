#!/usr/bin/env python3
"""session auth route module"""
from flask import jsonify, request, make_response, abort
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """setti/ng up checks for email and password"""
    print("Login endpoint hit!")
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    from models.user import User
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    from os import getenv
    session_name = getenv('SESSION_NAME')

    response = make_response(user.to_json())
    response.set_cookie(session_name, session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """logout"""
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    else:
        return jsonify({}), 200
