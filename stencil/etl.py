"""
(This is a file-level docstring.)
This file provides ETL (Extract Transform Load) functions for the NYC airbnb and NYC Taxi datasets.
"""
import csv
from time import sleep
from pymongo import MongoClient, TEXT, GEOSPHERE
from datetime import datetime


def loadAirbnb(file):
    """ Extract airbnb csv file into memory using CSV Reader
        Transform certain fields
        Load result into MongoDb using insert_many
        Create TEXT index on 'name' and 'neighbourhood'
        Create GEOSPHERE index on 'location'

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
    # TODO: Implement me


def loadTaxi(file):
    """ Extract taxi csv file into memory using CSV Reader
        Transform certain fields
        Load result into MongoDb using insert_many

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
    # TODO: Implement me


if __name__ == "__main__":
    db = MongoClient().test
    loadAirbnb('AB_NYC_2019.csv')
    loadTaxi('TAXI_NYC_2019.csv')
