"""
views.py

URL route handlers
"""

import urllib

from flask import jsonify

from application.decorators import login_required, admin_required
from models import User


##
# USER API
##

#@admin_required
def api_read_users():
    users = User.all()
    api_response = jsonify(ok=True, result=users)
    return api_response

#@admin_required
def api_create_user():
    user_email = request.form['email']
    entry = User.new(user_email)
    entry.email = user_email
    entry.name = request.form['name']
    entry.playlist = request.form['playlist']
    entry.videosPurchased = request.form['videosPurchased']
    entry.put()
    api_response = jsonify(ok=True)
    return api_response

#@login_required
def api_read_user(user_email):
    user_email = urllib.unquote(user_email)
    user = User.readByKey(user_email)
    api_response = jsonify(ok=True, result=user)
    return api_response

#@login_required
def api_update_user(user_email):
    User.update(user_email)
    api_response = jsonify(ok=True)
    return api_response

#@admin_required
def api_delete_user(user_email):
    User.delete(user_email)
    api_response = jsonify(ok=True)
    return api_response


##
# USER UI
##

#@admin_required
def delete_user():
    pass

#@admin_required
def get_user(user_name):
    user_query = User.query(ancestor=_users_key(user_name))
    user = user_query.fetch(1)
    return render_template('user.html', user=user)

#@admin_required
def create_user():
        user_name = self.request.get('user_name')

        user = User(parent=_users_key(user_name))

        user.playlist = self.request.get('playlist')
        user.put()

#@admin_required
def edit_user():
    pass

