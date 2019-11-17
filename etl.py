"""
(This is a file-level docstring.)
This file provides ETL (Extract Transform Load) functions for the NYC airbnb and NYC Taxi datasets.
"""
import csv
from time import sleep
from pymongo import MongoClient, TEXT, GEOSPHERE
from datetime import datetime


def loadAirbnb(file):
    """ Extract airbnb csv file into memory, Transform certain fields, and Load result into MongoDb using insert_many.
        Create TEXT index on 'name' and 'neighbourhood'.
        Create GEOSPHERE index on 'location'. 

        Schema:
            id - int
            name - string
            host_id - int
            host_name - string
            neighbourhood_group - string
            neighbourhood - string
            latitude - float
            longitude - float
            location - Point, coordinates[longitude, latitude] # https://docs.mongodb.com/manual/core/2dsphere/
            room_type - string
            price - int
            minimum_nights - int
            number_of_reviews - int
            last_review - string
            reviews_per_month - string
            calculated_host_listings_count - int
            availability_365 - int

    Args:
        file: location of the airbnb csv file.
    """
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = int(row['id'])
            row['host_id'] = int(row['host_id'])
            row['latitude'] = float(row['latitude'])
            row['longitude'] = float(row['longitude'])
            row['location'] = {'type': 'Point', 'coordinates': [
                row['longitude'], row['latitude']]}
            row['price'] = int(row['price'])
            row['minimum_nights'] = int(row['minimum_nights'])
            row['number_of_reviews'] = int(row['number_of_reviews'])
            row['calculated_host_listings_count'] = int(
                row['calculated_host_listings_count'])
            row['availability_365'] = int(row['availability_365'])

        inserted_ids = db.airbnb.insert_many(reader).inserted_ids
        db.airbnb.create_index(
            [('name', TEXT), ('neighbourhood', TEXT)], default_language='english')
        db.airbnb.create_index([('location', GEOSPHERE)])

        print("{} Airbnb docs inserted".format(len(inserted_ids)))
        print("Text index created for airbnb")
        print("Geosphere index created for airbnb")


def loadTaxi(file):
    """ Extract taxi csv file into memory, Transform certain fields, and Load result into MongoDb using insert_many.

        Schema:
            key - string
            fare_amount - float
            pickup_datetime - datetime
            pickup_longitude - float
            pickup_latitude - float
            dropoff_longitude - float
            dropoff_latitude - float
            passenger_count - int

    Args:
        file: location of the taxi csv file.
    """
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['fare_amount'] = float(row['fare_amount'])
            row['pickup_datetime'] = datetime.strptime(
                row['pickup_datetime'], '%Y-%m-%d %H:%M:%S %Z')
            row['pickup_longitude'] = float(row['pickup_longitude'])
            row['pickup_latitude'] = float(row['pickup_latitude'])
            row['dropoff_longitude'] = float(row['dropoff_longitude'])
            row['dropoff_latitude'] = float(row['dropoff_latitude'])
            row['passenger_count'] = int(row['passenger_count'])

        inserted_ids = db.taxi.insert_many(reader).inserted_ids
        print("{} taxi docs inserted".format(len(inserted_ids)))


if __name__ == "__main__":
    db = MongoClient().test
    loadAirbnb('AB_NYC_2019.csv')
    loadTaxi('TAXI_NYC_2019.csv')
