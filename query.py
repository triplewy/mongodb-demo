import csv
from pymongo import MongoClient

db = MongoClient().test

'''
    AirBNB Schema:
    _id, id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
    {'_id': ObjectId('5d992183589c75947f14835e'), 'id': '36444734', 'name': 'Sunny Upper West Side Apt. 3mins from Central Park', 'host_id': '32987938', 'host_name': 'Alex', 'neighbourhood_group': 'Manhattan', 'neighbourhood': 'Upper West Side', 'latitude': '40.77889', 'longitude': '-73.97668', 'room_type': 'Entire home/apt', 'price': '143', 'minimum_nights': '3', 'number_of_reviews': '0', 'last_review': '', 'reviews_per_month': '', 'calculated_host_listings_count': '1', 'availability_365': '10'}
'''

def query1():
    result = db.airbnb.find_one()

def query2():
    docs = db.airbnb.find({ 'neighbourhood' : 'Upper West Side' }, { '_id': 0, 'latitude': 1, 'longitude': 1, 'price': 1 })

    with open('query2.csv', 'w', newline='') as csvfile:
        fieldnames = ['latitude', 'longitude', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for doc in docs:
            writer.writerow(doc)

def query3():
    pass

def query4():
    pass

def query5():
    pass

if __name__ == "__main__":
    query2()