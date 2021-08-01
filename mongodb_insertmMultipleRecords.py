from pymongo import MongoClient


def insert_records(client):
    # Access database
    mydatabase = client["sampledb"]
    # Access collection of the database
    mycollection = mydatabase["sampletable"]

    # dictionary to be added in the database
    rec = records = {
            "record1": { "_id": 6,
            "name": "Anshul",
            "Roll No": "1006",
            "Branch": "CSE"},

            "record2": { "_id": 7,
            "name": "Abhinav",
            "Roll No": "1007",
            "Branch": "ME"}
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