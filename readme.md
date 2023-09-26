# Semantic search of wines

This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/semanticsearch-transformers-wines) and the [Hackernoon article: "Semantic Search Queries Return More Informed Results"](https://hackernoon.com/semantic-search-queries-return-more-informed-results-nr5335nw).

(TODO: Add demo video)

(TODO: Add Description)

The transformer model [`sentence-transformers/msmarco-distilroberta-base-v2`](https://huggingface.co/sentence-transformers/msmarco-distilroberta-base-v2) is connected to Weaviate as [vectorization module](https://www.semi.technology/developers/weaviate/current/modules/text2vec-transformers.html) (see `docker-compose.yaml` file).

## Prerequisites
(TO DO)

## Setup instructions
(TO DO) 

## Usage instructions
1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
2. Install requirements: `pip install -r requirements.txt`
3. Run `python import.py` to import 2500 wines to Weaviate.
4. Navigate to [console.semi.technology](https://console.semi.technology/), connect to `http://localhost:8080`, navigate to the query module, and happy querying!

## Dataset license
This folder contains Wine review data, retrieved from [Kaggle (from WineEnthusiast)](https://www.kaggle.com/zynicide/wine-reviews).
