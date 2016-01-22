"""
urls.py

URL dispatch route mappings and error handlers
"""

from application import app
from application import views


##
# URL dispatch rules
##

# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'home', view_func=views.home)

# Say hello
app.add_url_rule('/hello/<username>', 'say_hello', view_func=views.say_hello)

# Contrived admin-only
app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)

# list log entries
app.add_url_rule('/sys/logs', view_func=views.list_logs, methods=['GET'])



##
# User API
##
app.add_url_rule('/api/users', view_func=views.api_read_users, methods=['GET'])
app.add_url_rule('/api/user/<user_email>', view_func=views.api_read_user, methods=['GET'])
app.add_url_rule('/api/user', view_func=views.api_create_user, methods=['POST'])
app.add_url_rule('/api/user/<user_email>/delete', view_func=views.api_delete_user, methods=['POST'])
app.add_url_rule('/api/user/<user_email>/edit', view_func=views.api_update_user, methods=['PUT'])


##
# Playlist API
##
app.add_url_rule('/api/playlists', view_func=views.api_get_playlists, methods=['GET'])
app.add_url_rule('/api/playlists/<playlist_name>', view_func=views.api_get_playlist, methods=['GET'])
app.add_url_rule('/api/playlists', view_func=views.api_add_playlist, methods=['POST'])
app.add_url_rule('/api/playlists/<playlist_name>/delete', view_func=views.api_delete_playlist, methods=['POST'])
app.add_url_rule('/api/playlists/<int:playlist_id>/delete', view_func=views.api_delete_playlistById, methods=['POST'])

app.add_url_rule('/api/playlists/<playlist_name>/video/<int:video_id>', view_func=views.api_get_videoFromPlaylist, methods=['GET'])
app.add_url_rule('/api/playlists/<playlist_name>/video', view_func=views.api_add_videoToPlaylist, methods=['POST'])
app.add_url_rule('/api/playlists/<playlist_name>/video/<int:video_id>/delete', view_func=views.api_delete_videoFromPlaylist, methods=['POST'])


##
# Videos API
##
app.add_url_rule('/api/videos', view_func=views.api_get_videos, methods=['GET'])
app.add_url_rule('/api/videos', view_func=views.api_add_video, methods=['POST'])
app.add_url_rule('/api/videos/<int:video_id>', view_func=views.api_get_video, methods=['GET'])
app.add_url_rule('/api/videos/<int:video_id>/delete', view_func=views.api_delete_video, methods=['POST'])


##
# User UI
##
app.add_url_rule('/user/<int:user_id>', view_func=views.create_user, methods=['POST'])
app.add_url_rule('/user/<int:user_id>', view_func=views.get_user, methods=['GET'])
app.add_url_rule('/user/<int:user_id>/delete', view_func=views.delete_user, methods=['POST'])
app.add_url_rule('/user/<int:user_id>/edit', view_func=views.edit_user, methods=['PUT'])

##
# Playlist UI
##
app.add_url_rule('/playlist/<int:playlist_id>', view_func=views.add_video, methods=['POST'])
app.add_url_rule('/playlist/<int:playlist_id>', view_func=views.get_playlist, methods=['GET'])
app.add_url_rule('/playlist/<int:playlist_id>/delete', view_func=views.delete_video, methods=['POST'])
app.add_url_rule('/playlist/<int:playlist_id>/edit', view_func=views.edit_video, methods=['PUT'])


##
# Error handlers
##
from flask import render_template

# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

