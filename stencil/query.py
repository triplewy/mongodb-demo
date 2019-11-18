"""
(This is a file-level docstring.)
This file contains all required queries to MongoDb.
"""
from pymongo import MongoClient

db = MongoClient().test


def query1(minFare, maxFare):
    """ Finds taxi rides with fare amount greater than or equal to minFare and less than or equal to maxFare.  

    Args:
        minFare: An int represeting the minimum fare
        maxFare: An int represeting the maximum fare

    Projection:
        pickup_longitude
        pickup_latitude
        fare_amount

    Sort (Order matters):
        fare_amount - ascending
        pickup_latitude - descending
        pickup_longitude - descending

    Returns:
        An array of documents.

    Example:
        /query1?minFare=11&maxFare=11 -> [
            {
                "fare_amount": 11.0, 
                "pickup_latitude": 40.823625, 
                "pickup_longitude": -73.952692
            }, 
            {
                "fare_amount": 11.0, 
                "pickup_latitude": 40.818315, 
                "pickup_longitude": -73.960935
            },
            ...
        ]
    """
    # TODO: Implement me


def query2(textSearch, minReviews):
    """ Finds airbnbs with that match textSearch and have number of reviews greater than or equal to minReviews.  

    Args:
        textSearch: A str representing an arbitrary text search
        minReviews: An int represeting the minimum amount of reviews

    Projection:
        name
        number_of_reviews
        neighbourhood
        price

    Sort:
        price - ascending
        number_of_reviews - descending

    Returns:
        An array of documents.

    Example:
        /query2?search=coffee&minReviews=10 -> [
            {
                "name": "Coffee,Tea&Milk Astor Place Lodging", 
                "neighbourhood": "East Village", 
                "number_of_reviews": 125, 
                "price": 30
            }, 
            {
                "name": "Cozy Room For Two/ Steps to Train/Coffee included!", 
                "neighbourhood": "Harlem", 
                "number_of_reviews": 26, 
                "price": 54
            },
            ...
        ]
    """
    # TODO: Implement me


def query3():
    """ Groups airbnbs by neighbourhood_group and finds average price of each neighborhood_group sorted in descending order.  

    Projection:
        _id = neighbourhood_group
        avgPrice

    Sort:
        avgPrice - descending

    Returns:
        An array of documents.

    Example:
        /query3 -> [
            {
                "_id": "Manhattan", 
                "avgPrice": 196.8758136743456
            }, 
            {
                "_id": "Brooklyn", 
                "avgPrice": 124.38320732192598
            },
            ...
        ]
    """
    # TODO: Implement me


def query4():
    """ Aggregate taxis by pickup hour. 
        Find average fare for each hour.
        Find average manhattan distance travelled for each hour.
        Count total number of rides per pickup hour.
        Sort by average fare in descending order.

    Projection:
        _id = hour of pickup_datetime
        avgFare
        avgDistance (calculated using Manhattan Distance {abs(y2 - y1) + abs(x2 - x1)})
        count (Number of rides)

    Sort:
        avgFare - descending

    Returns:
        An array of documents.

    Example:
        /query4 -> [
            {
                "_id": 5, 
                "avgDistance": 0.07160818471929617, 
                "avgFare": 15.338208661417323, 
                "count": 508
            }, 
            {
                "_id": 4, 
                "avgDistance": 0.1281508752115708, 
                "avgFare": 13.740622950819674, 
                "count": 610
            }, 
            ...
        ]
    """
    # TODO: Implement me


def query5(latitude, longitude):
    """ Finds airbnbs within 1000 meters from location (longitude, latitude) using geoNear. 

    Args:
        latitude: A float representing latitude coordinate
        longitude: A float represeting longitude coordinate

    Projection:
        dist
        name
        neighbourhood
        neighbourhood_group
        price
        room_type

    Returns:
        An array of documents.

    Example:
        /query5?latitude=40.7829&longitude=-73.9654 -> [
            {
                "dist": {
                "calculated": 456.6389412208621
                }, 
                "name": "Sunny studio on UWS, steps to park", 
                "neighbourhood": "Upper West Side", 
                "neighbourhood_group": "Manhattan", 
                "price": 90, 
                "room_type": "Entire home/apt"
            }, 
            {
                "dist": {
                "calculated": 462.9532776699549
                }, 
                "name": "UWS Brownstone Near Central Park", 
                "neighbourhood": "Upper West Side", 
                "neighbourhood_group": "Manhattan", 
                "price": 212, 
                "room_type": "Entire home/apt"
            },
            ...
        ]
    """
    # TODO: Implement me
