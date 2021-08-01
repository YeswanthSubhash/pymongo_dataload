from pymongo import MongoClient

def get_data_with_limit(client):
    table_name = 'carsdetails'
    db = client['carsdb']
    table = db[table_name]

    cursor = table.find({}).limit(1)
    for record in cursor:
        print(record)



if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    #delete_records(client)
    #remove_all_records(client)
    get_data_with_limit(client)