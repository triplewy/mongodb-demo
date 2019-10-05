import csv
from time import sleep
from pymongo import MongoClient

import sys
import argparse

db = MongoClient().test

def loadCSV():
    result = []
    with open('AB_NYC_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result

def insertIntoMongo(arr):
    db.airbnb.insert_many([row for row in arr]).inserted_ids
    return db.airbnb.count_documents({})

if __name__ == "__main__":
    sleep(5)
    arr = loadCSV()
    numInserted = insertIntoMongo(arr)

    assert numInserted == len(arr)
