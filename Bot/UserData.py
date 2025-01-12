

from cachetools import LRUCache
import firebase_admin
from firebase_admin import firestore, credentials

# Used to allow for a custom evict callback
class CustomCache(LRUCache):
    def __init__(self, maxsize, getsizeof=None, evict=None):
        LRUCache.__init__(self, maxsize, getsizeof)
        self.__evict = evict
    def popitem(self):
        key, val = LRUCache.popitem(self)
        evict = self.__evict
        if evict:
            evict(key, val)
        return key, val


# Handles the access to the database
# handles both user and concert data
# Also caches the most recently used results
class UserData:
    
    def __init__(self):
        self.connected = False
        # connect to database
        self.connect()
        self.userCache = CustomCache(maxsize=10,evict=self.flushUserItem)
        self.concertCache = CustomCache(maxSize=100,evict=self.flushConcertItem)
    def connect(self):
        try:
            cred = credentials.Certificate('./serviceKey.json')
            app = firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self.connected = True
            print("Sucessfully connected to the database")
        except:
            print("Failed to connect to database")




    def getUserData(self,userId):
        # if there is no database entry or if it is malformed, we return an empty array for concert id
        if userId not in self.userCache:
            # attempt to retrieve
            doc_ref = self.db.collection('users').document(userId)
            concertIds = set()
            if doc_ref is not None:
                doc = doc_ref.get()
                if doc.exists:
                    userData = doc.to_dict()
                    if 'concerts' in userData:
                        concertIds = set(userData['concerts'])
                
            self.userCache[userId] = concertIds
        return self.userCache[userId]
    
    # add a concert for a user
    def addUserData(self,userId,concertID):
        concerts = self.getUserData(userId)
        concerts.add(concertID)
    
    # remove a concert for a user
    def removeUserData(self,userId,concertID):
        concerts = self.getUserData(userId)
        if concertID in concerts:
            concerts.remove(concertID)
        
    # use as eviction function for the user data
    def flushUserItem(self,key,value):
        user_ref = self.db.collection('users').document(key)
        user_ref.update({"concerts":list(value)})



    # flush the entire cache to the database
    def flushCache(self):
        self.userCache.clear()
        self.concertCache.clear()

