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

# Checking if the collection exists or not
if client.collection.exists("WineReviews") == False:
    raise Exception("Collection does not exist")

reviews = client.collection.get("WineReviews")

# Getting the user input from the user
user_query = input("Please enter the type of wine you are looking for: ")

# Querying the collection for the user input
query_response = reviews.query.near_text(
    user_query, 
    limit=10
)

print("-"*20)

print("The query response are as follows: \n")

for i in range(0, len(query_response.objects)):
    print(i+1)
    print("Title: " + query_response.objects[i].properties['title'] + "\n")
    print("Description: " + query_response.objects[i].properties['description'] + "\n")

print("-"*20)

# Getting the user input for the serial number of the wine to find similar wines
query_object = int(input("Enter the serial number of the wine to find similar wines: ")) - 1

# Querying the collection for similar wines
near_object_response = reviews.query.near_object(query_response.objects[query_object].metadata.uuid)

print("-"*20)

print("Similar wines are as follows: \n")

for i in range(0, len(near_object_response.objects)):
    print(i+1)
    print("Title: " + near_object_response.objects[i].properties['title'] + "\n")
    print("Description: " + near_object_response.objects[i].properties['description'] + "\n")

print("-"*20)