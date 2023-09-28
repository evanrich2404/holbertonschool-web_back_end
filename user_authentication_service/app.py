#!/usr/bin/env python3
"""Making basic Flask app"""
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def user():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, "email and password fields are required")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, "email and password fields are required")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
