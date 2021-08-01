from pymongo import MongoClient


def insert_records(client):
    # Access database
    mydatabase = client["sampledb"]
    # Access collection of the database
    mycollection = mydatabase["sampletable"]

    # dictionary to be added in the database
    rec = {
        'title': 'MongoDB and Python',
        'description': 'MongoDB is no SQL database',
        'tags': ['mongodb', 'database', 'NoSQL'],
        'viewers': 104
    }
    # inserting the data in the database
    mycollection.insert_one(rec)
    print(rec)


if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    insert_records(client)