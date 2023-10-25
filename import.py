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

# Deleting any prevously existing "DiseaseSearch" collections
print("delete previous")
print(client.collection.delete("DiseaseSearch"))

# Creating a new collection with the defined schema
client.collection.create(
    name="DiseaseSearch",
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
    vectorizer_config=wvc.ConfigFactory.Vectorizer.text2vec_transformers()
)

# Checking is the collection is created successfully or not
print("create new")
print(client.collection.exists("DiseaseSearch"))

# Importing the data using pandas
data = pd.read_csv('./data/disease.csv', index_col=0)

# Getting the collection "DiseaseSearch" that was created earlier
disease_data = client.collection.get("DiseaseSearch")

# Iterating through the disease dataset and storing it all in an array to be inserted later
desc_to_add = [
    wvc.DataObject(
        properties={
            "title": row["title"] + '.',
            "description": row["description"],
        },
    )
    for index, row in data.iterrows()
]

# Insertine the data into the collection
response = disease_data.data.insert_many(desc_to_add)
# print(response.errors) # Used to fetch if there are any errors while inserting the data into the collection

# Fetching any 2 Disease Data  from the collection and printing the response
response = disease_data.query.fetch_objects(limit=2)
print("Output")
print(response)