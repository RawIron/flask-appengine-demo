"""
models.py

App Engine datastore models
"""


from google.appengine.ext import ndb


class PurchaseLogMonthly(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    ofYearMonth = ndb.IntegerProperty(indexed=False)
    ofYear = ndb.IntegerProperty(indexed=False)
    ofMonth = ndb.IntegerProperty(indexed=False)

class PurchaseLogEntry(ndb.Model):
    purchasedOn = ndb.DateTimeProperty(auto_now_add=False)
    userName = ndb.StringProperty(indexed=False)
    videoName = ndb.StringProperty(indexed=False)
    videoPrice = ndb.IntegerProperty()


class UserCounters(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    lastLogin = ndb.DateTimeProperty(auto_now_add=True)
    videoWatchHistory = ndb.StringProperty()
    loginCounter = ndb.IntegerProperty()
    videoWatchCounter = ndb.IntegerProperty()


class GlobalCountersDaily(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    ofDay = ndb.DateProperty(auto_now_add=False)

class GlobalCountersTotal(ndb.Model):
    name = ndb.StringProperty(indexed=False)

class GlobalCounters(ndb.Model):
    videoWatchCounter = ndb.IntegerProperty()
    loginCounter = ndb.IntegerProperty()
    purchasesCounter = ndb.IntegerProperty()
    revenueCounter = ndb.IntegerProperty()

