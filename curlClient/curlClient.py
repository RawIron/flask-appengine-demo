import urllib
from curlWrapper import *


def sent(request):
    baseurl = 'http://localhost:8080'
    if request['method'] == 'GET':
        response = httpGet(baseurl + request['url'])
    elif request['method'] == 'POST':
        response = httpPost(baseurl + request['url'], request['payload'])
    elif request['method'] == 'PUT':
        response = httpPut(baseurl + request['url'], request['payload'])
    return response



def request_get_playlistByName(name):
    name = urllib.quote_plus(name)
    url = """/api/playlist/%s""" % (name, )
    request = {'method' : 'GET', 'url' : url}
    return request

def request_get_videoFromPlaylist(name, id):
    name = urllib.quote_plus(name)
    url = """/api/playlist/%s/video/%d""" % (name, id, )
    request = {'method' : 'GET', 'url' : url}
    return request

def request_delete_videoFromPlaylist(playlist_name, video_id):
    playlist_name = urllib.quote_plus(playlist_name)
    url = """/api/playlist/%s/video/%d/delete""" % (playlist_name, video_id, )
    payload = ''
    request = {'method' : 'POST', 'url' : url, 'payload' : payload}
    return request

def request_add_videoToPlaylist(playlist_name, video):
    playlist_name = urllib.quote_plus(playlist_name)
    url = """/api/playlist/%s/video""" % (playlist_name, )
    formData = {"name" : video['name'], "video_uri" : video['videoUri'], "tags" : video['tags'], }
    payload = urllib.urlencode(formData)
    request = {'method' : 'POST', 'url' : url, 'payload' : payload}
    return request


def get_playlistByName(playlist_name):
    request = request_get_playlistByName(playlist_name)
    response = sent(request)
    return response

def get_videoFromPlaylist(playlist_name, video_id):
    request = request_get_videoFromPlaylist(playlist_name, video_id)
    response = sent(request)
    return response

def delete_videoFromPlaylist(playlist_name, video):
    request = request_delete_videoFromPlaylist(playlist_name, video)
    response = sent(request)
    return response

def add_videoToPlaylist(playlist_name, video):
    request = request_add_videoToPlaylist(playlist_name, video)
    response = sent(request)
    return response

def delete_all_videosFromPlaylist(playlist_name):
    request = request_get_playlistByName(playlist_name)
    response = sent(request)
    if not response:
        print response
        return
    if response.has_key('ok') and not response['ok']:
        print response
        return
    if not response.has_key('result'):
        return
    videos = response['result']

    for video in videos:
        request = request_delete_videoFromPlaylist(playlist_name, video)
        sent(request)



def request_get_playlists():
    url = """/api/playlists"""
    request = {'method' : 'GET', 'url' : url}
    return request

def request_get_playlistsEntry(name):
    url = """/api/playlists/%s""" % (name, )
    request = {'method' : 'GET', 'url' : url}
    return request

def request_delete_playlistsEntry(name):
    url = """/api/playlists/%s/delete""" % (name, )
    payload = ""
    request = {'method' : 'POST', 'url' : url, 'payload' : payload}
    return request

def request_delete_playlistsEntryById(id):
    url = """/api/playlists/%s/delete""" % (id, )
    payload = ""
    request = {'method' : 'POST', 'url' : url, 'payload' : payload}
    return request

def request_add_playlistsEntry(entry):
    formData = {"name" : entry['name'], }
    payload = urllib.urlencode(formData)
    url = """/api/playlists"""
    request = {'method' : 'POST', 'url' : url, 'payload' : payload}
    return request


def count_playlists(): 
    request = request_get_playlists()
    response = sent(request)
    return len(response['result'].keys())

def get_playlists():
    request = request_get_playlists()
    response = sent(request)
    return response

def get_playlistsEntry(playlist_name):
    request = request_get_playlistsEntry(playlist_name)
    response = sent(request)
    return response

def delete_playlistsEntry(playlist_name):
    request = request_delete_playlistsEntry(playlist_name)
    response = sent(request)
    return response

def delete_playlistsEntryById(playlist_id):
    request = request_delete_playlistsEntryById(playlist_id)
    response = sent(request)
    return response

def add_playlistsEntry(entry):
    request = request_add_playlistsEntry(entry)
    response = sent(request)
    return response



def request_get_users():
    url = """/api/users"""
    request = {'method' : 'GET', 'url' : url}
    return request

def request_get_user(name):
    url = """/api/user/%s""" % (name, )
    request = {'method' : 'GET', 'url' : url}
    return request

def request_delete_user(name):
    url = """/api/user/%s/delete""" % (name, )
    payload = ""
    request = {'method' : 'POST', 'url' : url, 'payload' : payload}
    return request

def request_add_user(entry):
    payload = urllib.urlencode(entry)
    url = """/api/user"""
    request = {'method' : 'POST', 'url' : url, 'payload' : payload}
    return request


def get_users():
    request = request_get_users()
    response = sent(request)
    return response

def get_user(user_email):
    request = request_get_user(user_email)
    response = sent(request)
    return response

def delete_user(user_email):
    request = request_delete_user(user_email)
    response = sent(request)
    return response

def add_user(entry):
    request = request_add_user(entry)
    response = sent(request)
    return response



def run_batchOf(requests):
    for request in requests:
        response = sent(request)
        print response

