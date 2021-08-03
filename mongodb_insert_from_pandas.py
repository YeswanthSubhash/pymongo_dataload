from pymongo import MongoClient
import pandas as pd


if __name__== "__main__":

    petrol_data = pd.read_csv("sources/petrol.csv")
    print(petrol_data)

    client = MongoClient("mongodb://localhost:27017/")
    collection = client['cruds']['petrol']
    data = petrol_data.to_dict(orient='records')
    collection.insert_many(data)