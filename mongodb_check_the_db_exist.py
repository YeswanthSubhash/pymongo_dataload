from pymongo import MongoClient


def check_the_db_exists(client):
    list_of_db = client.list_database_names()
    print(list_of_db)

    if "sampledb" in list_of_db:
        print('sampledb is exists')



if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    check_the_db_exists(client)