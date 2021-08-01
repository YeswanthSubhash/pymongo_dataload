from pymongo import MongoClient
import sys

def get_data_equlaity(table):

    # To find() all the entries inside collection name 'carsTable'
    # Having Name 'chevrolet chevelle malibu'
    cursor = table.find({"Name": {"$eq": 'chevrolet chevelle malibu'}})
    for record in cursor:
        print(record)

def get_data_lessthan(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"Horsepower": {"$lt": 200}}, {'Name':1 ,'Horsepower': 1,'_id':0})
    for record in cursor:
        print(record)

def get_data_greaterthan(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"Horsepower": {"$gt": 200}}, {'Name':1 ,'Horsepower': 1,'_id':0})
    for record in cursor:
        print(record)

def get_data_lessthan_equalto(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"Horsepower": {"$lte": 95}}, {'Name':1 ,'Horsepower': 1,'_id':0})
    for record in cursor:
        print(record)

def get_data_greaterthan_equalto(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"Horsepower": {"$gte": 220}}, {'Name':1 ,'Horsepower': 1,'_id':0})
    for record in cursor:
        print(record)

def get_data_not_equalto(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"Origin": {"$ne": 'USA'}}, {'Name':1 ,'Origin': 1,'_id':0})
    for record in cursor:
        print(record)

def get_data_with_logical_and(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"$and": [{"Origin": {"$eq": "USA"}}, {"Horsepower": {"$gt": 200}}]},{"_id":0,"Origin": 1,"Horsepower": 1,"Name": 1})

    for record in cursor:
        print(record)

def get_data_with_logical_or(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"$or": [{"Origin": {"$eq": "USA"}}, {"Horsepower": {"$gt": 200}}]},{"_id":0,"Origin": 1,"Horsepower": 1,"Name": 1})

    for record in cursor:
        print(record)

def get_data_with_logical_not(table):
    # To find() Name and Horsepower the entries inside collection name 'carsdetails'
    # Having horsepower is less than 200
    cursor = table.find({"$not": [{"Origin": {"$eq": "USA"}}]},{"_id":0,"Origin": 1,"Horsepower": 1,"Name": 1})

    for record in cursor:
        print(record)





if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        table_name = 'carsdetails'
        db = client['carsdb']
        table = db[table_name]
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    #get_data_equlaity(table)
    #get_data_lessthan(table)
    #get_data_greaterthan(table)
    #get_data_greaterthan_equalto(table)
    #get_data_lessthan_equalto(table)
    #get_data_not_equalto(table)
    #get_data_with_logical_and(table)
    #get_data_with_logical_or(table)
    get_data_with_logical_not(table)