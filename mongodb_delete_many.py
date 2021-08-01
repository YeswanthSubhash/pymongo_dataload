from pymongo import MongoClient

def delete_records(client):

    table_name = 'studentTable'
    db = client['sampledb']
    table = db[table_name]

    # Total Number of Records.
    total_count = table.count_documents({})
    print(total_count)

    # Deleted number of records.
    result = table.delete_one({"_id": 1})
    print(result.deleted_count)


    total_count_after_del = table.count_documents({})
    print(total_count_after_del)

def remove_all_records(client):
    table_name = 'studentTable'
    db = client['sampledb']
    table = db[table_name]

    # Total Number of Records.
    total_count = table.count_documents({})
    print(total_count)

    # Deleted number of records.
    result = table.remove()
    print(result)

    total_count_after_del = table.count_documents({})
    print(total_count_after_del)

def drop_collections(client):
    table_name = 'studentTable'
    db = client['sampledb']
    table = db[table_name]

    table.drop()





if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    #delete_records(client)
    #remove_all_records(client)
    drop_collections(client)