from pymongo import MongoClient




def delete_records_regex(client):
    table_name = 'carsdetails'
    db = client['carsdb']
    table = db[table_name]

    select_query = {"Name": {"$regex": "^c"}}
    cursor = table.find(select_query)
    for record in cursor:
        print(record)

    result = table.delete_many(select_query)
    print(result.deleted_count)

    cursor = table.find(select_query)
    for record in cursor:
        print(record)






if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")

    delete_records_regex(client)
