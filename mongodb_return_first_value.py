from pymongo import MongoClient
import sys

def get_first_value_from_table(client):

    table_name = 'carsTable'
    db = client['sampledb']
    table = db[table_name]

    # To find() all the entries inside collection name 'myTable'
    record = table.find_one()
    print(record)


if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    get_first_value_from_table(client)