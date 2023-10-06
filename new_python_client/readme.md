# Semantic search of wines

This is the implementation of the "wine search" demo using weaviate's new python client ["Collections"](https://weaviate.io/developers/weaviate/client-libraries/experimental). It allows easier interaction with the weaviate client with shorted code snippets for CRUD operations. It allows strong typing through custom Python classes as defined by Weaviate instead of using untyped dict/JSONs as done previously. It also allows to interact with individual collections instead of entire database. This leads to much simpler and more focused development. You can read about it's other features in the "Collections" doc linked above.

## Prerequisites
Before you can run the project, you need to have Docker, Docker Compose, and Python installed on your machine. You can follow along the installation instructions [here](./../readme.md).

## Setup instructions
Please make sure that you are setting up the environment in the new directory called "new_python_client" and not in the main directory.
1. **Install virtualenv** (if not already installed):
   ```bash
   pip install virtualenv
   ```
2. **Create a Virtual Environment:** 
   Navigate to the directory where you want to create your virtual environment, then run:
   ```bash
   virtualenv <name_of_virtualenv>
   ```
3. **Activate the Virtual Environment:** 
   On Windows, run:
   ```bash
   .\<name_of_virtualenv>\Scripts\activate
   ```
   On macOS and Linux, run:
   ```bash
   source <name_of_virtualenv>/bin/activate
   ```
4. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage instructions
Please make sure that you are setting up the environment in the new directory called "new_python_client" and not in the main directory. The compose file is different and contains some extra instructions to support 'collections'.

1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
2. Run `python import.py` to import 2500 wines to Weaviate.
3. The data is now stored in the weaviate client. You can experiment with it using a python notebook or a python file.

## Dataset license
This folder contains Wine review data, retrieved from [Kaggle (from WineEnthusiast)](https://www.kaggle.com/zynicide/wine-reviews).

## Notes:
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/semanticsearch-transformers-wines) and the [Hackernoon article: "Semantic Search Queries Return More Informed Results"](https://hackernoon.com/semantic-search-queries-return-more-informed-results-nr5335nw).
