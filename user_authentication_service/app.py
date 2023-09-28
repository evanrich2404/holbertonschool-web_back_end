#!/usr/bin/env python3
"""Making basic Flask app"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    """Root route that welcomes users.

    Returns:
        A message welcoming the user.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def user():
    """Registers a new user.

    The request must contain "email" and "password" fields.
    If the user is already registered, a 400 error is returned.

    Returns:
        JSON object containing the registered user's
        email and a success message.
    """
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
    """Logs in a user.

    The request must contain "email" and "password" fields.
    Upon successful login, a session cookie is set.

    Returns:
        JSON object with the user's email and a success message if logged in.
    """
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


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logs out a user.

    Deletes the user's session based on their session ID cookie.

    Returns:
        Redirects to the root route upon successful logout.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """Fetches the profile of the logged-in user.

    Returns:
        JSON object with the user's email.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Generates a password reset token for the user.

    The request must contain an "email" field. If the email is found,
    a reset token is generated.

    Returns:
        JSON object containing the email and generated reset token.
    """
    email = request.form.get("email")

    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Updates the user's password using the provided reset token.

    The request must contain "email", "reset_token", and "new_password" fields.

    Returns:
        JSON object with the user's email
        and a success message upon successful password update.
    """
    email = request.form.get("email")
    token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    """Main execution of the Flask app when run as a script.

    The app will run on all available network interfaces (0.0.0.0)
    and will listen on port 5000 by default.
    """
    app.run(host="0.0.0.0", port="5000")
