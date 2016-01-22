"""
models.py

App Engine datastore models
"""


from google.appengine.ext import ndb


class BookOfNames(ndb.Model):

    name = ndb.StringProperty(required=True, indexed=True)
    createdAt = ndb.DateTimeProperty(indexed=False, auto_now_add=True)

    @classmethod
    def all(cls):
        names = []
        for entry in cls.query():
            a_name = cls._createDictionaryFrom(entry)
            names.append(a_name)
        return names

    @classmethod
    def byKey(cls, find_name):
        result = cls.query(BookOfNames.name == find_name)
        if result is None:
            return {}
        entry = result.get()
        a_name = cls._createDictionaryFrom(entry)
        return a_name

    @classmethod
    def delete(cls, delete_name):
        result = cls.query(BookOfNames.name == delete_name)
        if result is None:
            return False
        entry = result.get()
        entry.key.delete()
        return True

    @classmethod
    def deleteByKey(cls, id_ofName):
        key = ndb.Key(BookOfNames, id_ofName)
        key.delete()
        return True

    @classmethod
    def _createDictionaryFrom(cls, entry):
        if entry is None:
            return {}
        show = {}
        show['kind'] = entry.key.kind()
        show['id'] = entry.key.id()
        show['name'] = entry.name
        return show

