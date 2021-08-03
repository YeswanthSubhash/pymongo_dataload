from pymongo import MongoClient
import pandas as pd


if __name__== "__main__":

    # point the client at mongo URI
    client = MongoClient("mongodb://localhost:27017/")
    # select database
    db = client['cruds']
    # select the collection within the database
    test = db['petrol']
    # convert entire collection to Pandas dataframe
    data = pd.DataFrame(list(test.find()))

    print(data)