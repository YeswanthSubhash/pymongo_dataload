from pymongo import MongoClient


def insert_records(client):
    # Access database
    mydatabase = client["sampledb"]
    # Access collection of the database
    mycollection = mydatabase["carsTable"]

    # dictionary to be added in the database
    mylist = [
        {"Manufacturer": "Honda", "Model": "City", "Color": "Black"},
        {"Manufacturer": "Tata", "Model": "Altroz", "Color": "Golden"},
        {"Manufacturer": "Honda", "Model": "Civic", "Color": "Red"},
        {"Manufacturer": "Hyundai", "Model": "i20", "Color": "white"},
        {"Manufacturer": "Maruti", "Model": "Swift", "Color": "Blue"},
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