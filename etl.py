import csv
from time import sleep
from pymongo import MongoClient, TEXT, GEOSPHERE
from datetime import datetime


def loadAirbnb():
    arr = []
    with open('AB_NYC_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['price'] = int(row['price'])
            row['number_of_reviews'] = int(row['number_of_reviews'])
            row['latitude'] = float(row['latitude'])
            row['longitude'] = float(row['longitude'])
            row['location'] = {'type': 'Point', 'coordinates': [row['longitude'], row['latitude']]}
            del row['latitude']
            del row['longitude']
            arr.append(row)

    inserted_ids = db.airbnb.insert_many(arr).inserted_ids
    return len(inserted_ids)


def loadTaxi():
    arr = []
    with open('TAXI_NYC_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['fare_amount'] = float(row['fare_amount'])
            row['pickup_longitude'] = float(row['pickup_longitude'])
            row['pickup_latitude'] = float(row['pickup_latitude'])
            row['dropoff_longitude'] = float(row['dropoff_longitude'])
            row['dropoff_latitude'] = float(row['dropoff_latitude'])
            row['pickup_datetime'] = datetime.strptime(row['pickup_datetime'], '%Y-%m-%d %H:%M:%S %Z')
            arr.append(row)

    inserted_ids = db.taxi.insert_many(arr).inserted_ids
    return len(inserted_ids)


if __name__ == "__main__":
    db = MongoClient().test
    numAB = loadAirbnb()
    print("{} Airbnb docs inserted".format(numAB))
    numTaxi = loadTaxi()
    print("{} taxi docs inserted".format(numTaxi))
    db.airbnb.create_index([('name', TEXT), ('neighbourhood', TEXT)], default_language='english')
    print("Text index created for airbnb")
    db.airbnb.create_index([('location', GEOSPHERE)])
    print("Geosphere index created for airbnb")
