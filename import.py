import weaviate
from weaviate import Config
import weaviate.classes as wvc
import os
import pandas as pd

# Starting up the weaviate client
client = weaviate.Client(
    "http://localhost:8080",
    additional_config=Config(grpc_port_experimental=50051),
)

# Deleting any prevously existing "Wine" collections
print(client.collection.delete("Wine"))

# Creating a new collection with the defined schema
articles = client.collection.create(
    name="Wine",
    properties=[
        wvc.Property(
            name="title",
            data_type=wvc.DataType.TEXT,
        ),
        wvc.Property(
            name="description",
            data_type=wvc.DataType.TEXT,
        )
    ],
)

# Checking is the collection is created successfully or not
print(client.collection.exists("Wine"))

# Importing the data using pandas
data = pd.read_csv('./data/wine_reviews.csv', index_col=0)

# Getting the collection "Wine" that was created earlier
wine_collection = client.collection.get("Wine")

# Iterating through the wine_reviews dataset and storing it all in an array to be inserted later
wines_to_add = [
    wvc.DataObject(
        properties={
            "title": row["title"] + '.',
            "description": row["description"],
        },
    )
    for index, row in data.iterrows()
]

# Insertine the data into the collection
response = wine_collection.data.insert_many(wines_to_add)
# print(response.errors) # Used to fetch if there are any errors while inserting the data into the collection

# Fetching any 2 wine reviews from the collection and printing the response
response = wine_collection.query.fetch_objects(limit=2)
print(response)