from pymongo import MongoClient

def get_data(client):

    table_name = 'carsdetails'
    db = client['carsdb']
    table = db[table_name]

    # Before Creating index
    index_list = sorted(list(table.index_information()))
    print("Before Creating index")
    print(index_list)

    #drop index
    table.drop_index('_id_')

    # Creating index
    table.create_indexes("Name", Unique = False)

    # After Creating index
    index_list = sorted(list(table.index_information()))
    print("\After Creating index")
    print(index_list)





if __name__ ==  "__main__":
    # creation of MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print('Connected Sucessfully')
    except:
        print("Could not connect to mongo db")
    get_data(client)