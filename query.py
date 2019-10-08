from pymongo import MongoClient

db = MongoClient().test

'''
    AirBNB Schema:
    id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
    2539,Clean & quiet apt home by the park,2787,John,Brooklyn,Kensington,40.64749,-73.97237,Private room,149,1,9,2018-10-19,0.21,6,365


    Taxi Schema:
    key, pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count
    2011-10-08 11:53:44.0000002,2011-10-08 11:53:44 UTC,-73.982524,40.75126,-73.979654,40.746139,1
'''


def query1():
    docs = db.airbnb.distinct('neighbourhood')
    result = [doc for doc in docs]
    return result


def query2():
    docs = db.airbnb.find({'neighbourhood': 'Upper West Side'}, {
                          '_id': 0, 'latitude': 1, 'longitude': 1, 'price': 1})
    result = [doc for doc in docs]
    return result


def query3():
    docs = db.airbnb.aggregate([{'$group': {'neighbourhood': '$neighbourhood', 'avgPrice': {'$avg': '$price'}}}, {'$sort': {'avgPrice': 1}}])
    result = [doc for doc in docs]
    return result


def query4():
    pass


def query5():
    pass
