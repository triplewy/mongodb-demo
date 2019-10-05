from pymongo import MongoClient

db = MongoClient().test

def query1():
    result = db.airbnb.find_one()
    print(result)

def query2():
    docs = db.airbnb.find({ 'neighbourhood' : 'Upper West Side' })
    for doc in docs:
        print(doc)

def query3():
    pass

def query4():
    pass

if __name__ == "__main__":
    query1()
    query2()