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



class Video(ndb.Model):

    name = ndb.StringProperty(required=True, indexed=True)
    videoUri = ndb.StringProperty(indexed=False)
    available = ndb.BooleanProperty(indexed=False, default=True)
    tags = ndb.StringProperty(repeated=True)
    createdAt = ndb.DateTimeProperty(indexed=False, auto_now_add=True)

    @classmethod
    def byKey(cls, video_id):
        key = ndb.Key(Video, video_id)
        entry = key.get()
        video = cls._createDictionaryFrom(entry)
        return video

    @classmethod
    def all(cls):
        videos = []
        for entry in cls.query():
            video = cls._createDictionaryFrom(entry)
            videos.append(video)
        return videos

    @classmethod
    def delete(cls, video_id):
        key = ndb.Key(Video, video_id)
        try:
            key.delete()
        except CapabilityDisabledError:
            pass

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

