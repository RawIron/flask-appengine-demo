"""
views.py

URL route handlers
"""

from flask import jsonify

from models import BookOfNames
from decorators import *


##
# BookOfNames API
##

@login_not_required
def api_get_bookOfNames():
    names = BookOfNames.all()
    api_response = jsonify(ok=True, result=names)
    return api_response

def api_get_fromBook(this_name):
    a_name = Playlists.byKey(this_name)
    api_response = jsonify(ok=True, result=a_name)
    return api_response

def api_add_nameToBook():
    name = request.form['name']
    entry = BookOfNames(name = name)
    entry.put()
    api_response = jsonify(ok=True, result=request.form)
    return api_response

def api_delete_fromBook(this_name):
    BookOfNames.delete(this_name)
    api_response = jsonify(ok=True)
    return api_response

def api_delete_fromBookById(id_ofName):
    BookOfNames.deleteByKey(id_ofName)
    api_response = jsonify(ok=True)
    return api_response

