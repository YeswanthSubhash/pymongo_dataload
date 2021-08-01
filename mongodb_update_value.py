from pymongo import MongoClient

def get_data(client):

    table_name = 'car_details'
    db = client['sampledb']
    table = db[table_name]

    # To find() all the entries inside collection name 'myTable'
    cursor = table.find()
    for record in cursor:
        print(record)

def update_data(client):
    table_name = 'car_details'
    db = client['sampledb']
    table = db[table_name]

    # To find() all the entries inside collection name 'myTable'
    filter = {'_id': 1}
    new_values = {'$set':{'name':'Yeswanth','Roll No':'1005'}}
    #cursor = table.find(filter)
    table.update_one(filter,new_values)







if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    get_data(client)
    update_data(client)
    get_data(client)