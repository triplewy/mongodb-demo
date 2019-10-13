from pymongo import MongoClient

db = MongoClient().test


def query1(minFare, maxFare):
    docs = db.taxi.find(
        {
            'fare_amount': {
                '$gte': minFare,
                '$lte': maxFare
            }
        },
        {
            '_id': 0,
            'pickup_longitude': 1,
            'pickup_latitude': 1,
            'fare_amount': 1
        }
    )

    result = [doc for doc in docs]
    return result


def query2(textSearch, minReviews):
    docs = db.airbnb.find(
        {
            '$text': {
                '$search': textSearch
            },
            'number_of_reviews': {
                '$gte': minReviews
            }
        },
        {
            '_id': 0,
            'name': 1,
            'number_of_reviews': 1,
            'neighbourhood': 1,
            'price': 1
        }
    )

    result = [doc for doc in docs]
    return result


def query3():
    docs = db.airbnb.aggregate([
        {
            '$group': {
                '_id': '$neighbourhood_group',
                'avgPrice': {
                    '$avg': '$price'
                }
            }
        },
        {
            '$sort': {'avgPrice': -1}
        }
    ])

    result = [doc for doc in docs]
    return result


def query4():
    docs = db.taxi.aggregate([
        {
            '$group': {
                '_id': {'$hour': "$pickup_datetime"},
                'avgFare': {'$avg': '$fare_amount'},
                'avgDistance': {
                    '$avg': {
                        '$add': [
                            {'$abs': {'$subtract': ['$pickup_latitude', '$dropoff_latitude']}},
                            {'$abs': {'$subtract': ['$pickup_longitude', '$dropoff_longitude']}}
                        ]
                    }
                },
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'avgFare': -1}
        }
    ])
    result = [doc for doc in docs]
    return result


def query5():
    docs = db.airbnb.aggregate([
        {
            '$geoNear': {
                'near': {'type': 'Point', 'coordinates': [-73.9654, 40.7829]},
                'distanceField': 'dist.calculated',
                'maxDistance': 1000,
                'includeLocs': 'dist.location',
                'spherical': False
            }
        },
        {
            '$project': {
                '_id': 0,
                'dist': 1,
                'location': 1,
                'name': 1,
                'neighbourhood': 1,
                'neighbourhood_group': 1,
                'price': 1,
                'room_type': 1
            }
        }
    ])
    result = [doc for doc in docs]
    return result
