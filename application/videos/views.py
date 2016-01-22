"""
views.py

URL route handlers
"""

from models import Playlists, PlaylistEntry, Video
from flask import jsonify
from application.decorators import *


def api_get_videos():
    videos = Video.all()
    api_response = jsonify(ok=True, result=videos)
    return api_response

def api_add_video():
    entry = Video()
    entry.name = request.form['name']
    entry.videoUri = request.form['video_uri']
    entry.put()
    api_response = jsonify(ok=True)
    return api_response

def api_delete_video(video_id):
    Video.delete(video_id)
    api_response = jsonify(ok=True)
    return api_response

def api_search_video():
    pass

