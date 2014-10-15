import pymongo

class dboperation(object):
    """manipulate mongodb"""
    
    def __init__(self, arg='test'):
        conn = pymongo.Connection("localhost",27017)
        self.db = conn[arg]

    def insert(self,dicts):

        coll = self.db.userinfos
        coll.insert(dicts)
        return 1

    def find_one(self,key):
        coll = self.db.userinfos
        return coll.find_one(key)



if __name__ == "__main__":
    db = dboperation()
    db.insert( dict({"name":"123"}))
    res = db.find_one({"name":"123"})
    print res









