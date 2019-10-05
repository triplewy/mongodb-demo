import csv
from time import sleep
from pymongo import MongoClient


def loadAirbnb():
    arr = []
    with open('AB_NYC_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arr.append(row)

    inserted_ids = db.airbnb.insert_many(arr).inserted_ids
    return len(inserted_ids)


def loadTaxi():
    arr = []
    with open('TAXI_NYC_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arr.append(row)

    inserted_ids = db.taxi.insert_many(arr).inserted_ids
    return len(inserted_ids)


if __name__ == "__main__":
    db = MongoClient().test
    numAB = loadAirbnb()
    numTaxi = loadTaxi()

    print("{} Airbnb docs inserted".format(numAB))
    print("{} taxi docs inserted".format(numTaxi))
