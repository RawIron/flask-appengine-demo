"""
models.py

App Engine datastore models
"""


from google.appengine.ext import ndb


# We set the same parent key on the 'User' to ensure one user
# per entity group. Queries across the single entity group
# will be consistent. However, the write rate to a single entity group
# should be limited to ~1/second.

def _user_key(user_email):
    """Constructs a Datastore key for a user entity"""
    key = ndb.Key(user_email, user_email)
    return key

class User(ndb.Model):
    googleUser = ndb.UserProperty()
    email = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(indexed=False)
    playlist = ndb.StringProperty(indexed=False)
    videosPurchased = ndb.StringProperty(indexed=False)
    createdAt = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def all(cls):
        users = []
        for entry in cls.query():
            user = cls._createDictionaryFrom(entry)
            users.append(user)
        return users

    @classmethod
    def new(cls, user_email):
        ancestor_key = _user_key(user_email)
        return User(parent=ancestor_key)

    @classmethod
    def readByKey(cls, user_email):
        ancestor_key = _user_key(user_email)
        result = cls.query(User.email == user_email, ancestor=ancestor_key)
        if result is None:
            return {}
        entry = result.get()
        user = cls._createDictionaryFrom(entry)
        return user

    @classmethod
    def delete(cls, user_email):
        ancestor_key = _user_key(user_email)
        result = cls.query(User.email == user_email, ancestor=ancestor_key)
        if result is None:
            return False
        entry = result.get()
        entry.key.delete()
        return True

    @classmethod
    def update(cls, user_email):
        pass

    @classmethod
    def _createDictionaryFrom(cls, entry):
        if entry is None:
            return {}
        user = {}
        user['parentId'] = entry.key.parent().id()
        user['parentKind'] = entry.key.parent().kind()
        user['id'] = entry.key.id()
        user['kind'] = entry.key.kind()
        user['email'] = entry.email
        user['name'] = entry.name
        user['playlist'] = entry.playlist
        user['videosPurchased'] = entry.videosPurchased
        return user


class UserRawJson(ndb.Model):
    email = ndb.StringProperty(indexed=True, required=True)
    content = ndb.JsonProperty(indexed=False)

class UserRawPickle(ndb.Model):
    email = ndb.StringProperty(indexed=True, required=True)
    content = ndb.PickleProperty(indexed=False)

