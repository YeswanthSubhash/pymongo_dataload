from pymongo import MongoClient


def insert_records(client):
    # Access database
    mydatabase = client["sampledb"]
    # Access collection of the database
    mycollection = mydatabase["studentTable"]

    # dictionary to be added in the database
    mylist = [
        {"_id": 1, "name": "Vishwash", "Roll No": "1001", "Branch": "CSE"},
        {"_id": 2, "name": "Vishesh", "Roll No": "1002", "Branch": "IT"},
        {"_id": 3, "name": "Shivam", "Roll No": "1003", "Branch": "ME"},
        {"_id": 4, "name": "Yash", "Roll No": "1004", "Branch": "ECE"},
    ]
    # inserting the data in the database
    mycollection.insert_many(mylist)
    print(mylist)


if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    insert_records(client)