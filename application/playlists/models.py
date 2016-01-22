"""
models.py

App Engine datastore models
"""


from google.appengine.ext import ndb


# We set the same parent key on the 'Playlist' to ensure one playlist
# per entity group. Queries across the single entity group
# will be consistent. However, the write rate to a single entity group
# should be limited to ~1/second.

def _playlists_key(playlist_name):
    """Constructs a Datastore key for a playlist entity"""
    key = ndb.Key(playlist_name, playlist_name)
    return key


class Playlists(ndb.Model):

    name = ndb.StringProperty(required=True, indexed=True)
    videoUri = ndb.StringProperty(indexed=False)
    available = ndb.BooleanProperty(indexed=False, default=True)
    tags = ndb.StringProperty(repeated=True)
    createdAt = ndb.DateTimeProperty(indexed=False, auto_now_add=True)

    @classmethod
    def all(cls):
        playlists = []
        for entry in cls.query():
            playlist = cls._createDictionaryFrom(entry)
            playlists.append(playlist)
        return playlists

    @classmethod
    def new(cls, playlist_name):
        ancestor_key = _playlists_key(playlist_name)
        return Playlists(parent=ancestor_key)

    @classmethod
    def byKey(cls, playlist_name, video_id):
        ancestor_key = _playlists_key(playlist_name)
        key = ndb.Key(Playlists, video_id, parent=ancestor_key)
        entry = key.get()
        video = cls._createDictionaryFrom(entry)
        return video

    @classmethod
    def allVideos(cls, playlist_name):
        ancestor_key = _playlists_key(playlist_name)
        videos = []
        for entry in cls.query(ancestor=ancestor_key):
            video = cls._createDictionaryFrom(entry)
            videos.append(video)
        return videos

    @classmethod
    def deleteVideo(cls, playlist_name, playlist_id):
        ancestor_key = _playlists_key(playlist_name)
        key = ndb.Key(Playlists, playlist_id, parent=ancestor_key)
        key.delete()

    @classmethod
    def _createDictionaryFrom(cls, entry):
        if entry is None:
            return {}
        video = {}
        video['parentId'] = entry.key.parent().id()
        video['parentKind'] = entry.key.parent().kind()
        video['id'] = entry.key.id()
        video['kind'] = entry.key.kind()
        video['name'] = entry.name
        video['videoUri'] = entry.videoUri
        return video

