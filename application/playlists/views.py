"""
views.py

URL route handlers
"""

from models import Playlists, PlaylistEntry, Video
from flask import jsonify
from application.decorators import *


##
# PLAYLIST API
##

@login_not_required
def api_get_playlistNames():
    playlists = Playlists.all()
    api_response = jsonify(ok=True, result=playlists)
    return api_response

def api_get_playlistName(playlist_name):
    playlistsEntry = Playlists.byKey(playlist_name)
    api_response = jsonify(ok=True, result=playlistsEntry)
    return api_response

def api_add_playlist():
    name = request.form['name']
    entry = Playlists(name = name)
    entry.put()
    api_response = jsonify(ok=True, result=request.form)
    return api_response

def api_delete_playlist(playlist_name):
    Playlists.delete(playlist_name)
    api_response = jsonify(ok=True)
    return api_response

def api_delete_playlistById(playlist_id):
    Playlists.deleteByKey(playlist_id)
    api_response = jsonify(ok=True)
    return api_response

def api_get_playlist(playlist_name):
    videos = PlaylistEntry.all(playlist_name)
    api_response = jsonify(ok=True, result=videos)
    return api_response

def api_add_videoToPlaylist(playlist_name):
    entry = PlaylistEntry.new(playlist_name)
    entry.name = request.form['name']
    entry.videoUri = request.form['video_uri']
    entry.put()
    api_response = jsonify(ok=True)
    return api_response

def api_get_videoFromPlaylist(playlist_name, video_id):
    video = PlaylistEntry.byKey(playlist_name, video_id)
    api_response = jsonify(ok=True, result=video)
    return api_response

def api_delete_videoFromPlaylist(playlist_name, video_id):
    PlaylistEntry.delete(playlist_name, video_id)
    api_response = jsonify(ok=True)
    return api_response



##
# PLAYLIST UI
##
#@admin_required
def get_playlist(playlist_name):
    videos = PlaylistEntry.all(playlist_name)
    return render_template('playlist.html', videos=videos)

#@admin_required
def delete_video(playlist_name, playlist_id):
    PlaylistEntry.delete(playlist_id)

#@admin_required
def add_video(playlist_name):
    entry = PlaylistEntry.new(playlist_name)
    entry.name = form.data.get('name')
    entry.video = form.data.get('video_uri')
    entry.put()

#@admin_required
def edit_video(playlist_name, playlist_id):
    entry = PlaylistEntry.byId(playlist_name, playlist_id)
    entry.name = form.data.get('name')
    entry.video = form.data.get('video_uri')
    entry.put()

