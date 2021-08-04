from pymongo import MongoClient

def get_data(client):

    table_name = 'carsdetails'
    db = client['carsdb']
    table = db[table_name]

    agg_pipeline = [
        {"$match": {"Origin": "USA"}},
        {"$group":{"_id": None,"count": {"$sum" : 1}

            }
         }

    ]

    # To find() all the entries inside collection name 'myTable'
    cursor = table.aggregate(agg_pipeline)
    for record in cursor:
        print(record)


if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    get_data(client)