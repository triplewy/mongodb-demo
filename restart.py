from pymongo import MongoClient


def restartMongo():
    db = MongoClient().test
    db.airbnb.drop()
    db.taxi.drop()

if __name__ == "__main__":
    restartMongo()
