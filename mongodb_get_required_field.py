from pymongo import MongoClient
import sys

def get_required_fields(client):

    table_name = 'carsTable'
    db = client['sampledb']
    table = db[table_name]

    # To select required field by passing 1 for required and 0 for non required fields'
    cursor = table.find({},{"_id":0,"Manufacturer":1,"Model":1,"Color":1})
    for record in cursor:
        print(record)


if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    get_required_fields(client)