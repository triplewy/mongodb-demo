import csv
from time import sleep
from pymongo import MongoClient, TEXT


def loadAirbnb():
    arr = []
    with open('AB_NYC_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['price'] = int(row['price'])
            row['number_of_reviews'] = int(row['number_of_reviews'])
            row['latitude'] = float('%.3f' % (row['latitude']))
            row['longitude'] = float('%.3f' % (row['longitude']))
            arr.append(row)

    inserted_ids = db.airbnb.insert_many(arr).inserted_ids
    return len(inserted_ids)


def loadTaxi():
    arr = []
    with open('TAXI_NYC_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['fare_amount'] = float(row['fare_amount'])
            row['pickup_longitude'] = float('%.3f' % (row['pickup_longitude']))
            row['pickup_latitude'] = float('%.3f' % (row['pickup_latitude']))
            row['dropoff_longitude'] = float('%.3f' % (row['dropoff_longitude']))
            row['dropoff_latitude'] = float('%.3f' % (row['dropoff_latitude']))
            arr.append(row)

    inserted_ids = db.taxi.insert_many(arr).inserted_ids
    return len(inserted_ids)


if __name__ == "__main__":
    db = MongoClient().test
    numAB = loadAirbnb()
    numTaxi = loadTaxi()
    db.airbnb.create_index([('name', TEXT)], default_language='english')
    db.airbnb.create_index([('neighbourhood', TEXT)], default_language='english')

    print("{} Airbnb docs inserted".format(numAB))
    print("{} taxi docs inserted".format(numTaxi))
