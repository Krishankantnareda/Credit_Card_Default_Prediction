from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
uri = "mongodb+srv://KrishankantNareda:KrishankantNareda@cluster1.efnqv2t.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="Credit_Card_F"
COLLECTION_NAME="Data"

# read the data as a dataframe
df = pd.read_csv(r"notebooks\data\UCI_Credit_Card_modified.csv")
df = df.drop(columns='ID')

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

print(json_record)
#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)