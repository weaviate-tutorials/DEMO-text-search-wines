# Semantic search of wines

In this repository, you'll find the practical essence of the article [Hackernoon article: "Semantic Search Queries Return More Informed Results"](https://hackernoon.com/semantic-search-queries-return-more-informed-results-nr5335nw) distilled into code (albeit updated). The author points out a common hurdle: the struggle with searching through our own unstructured data. Weaviate, an open-source vector search engine, is introduced as a sturdy bridge over this hurdle. Following the narrative, this codebase sets up Weaviate, harnesses the open transformer model [`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) for vectorization through the [vectorization module](https://www.semi.technology/developers/weaviate/current/modules/text2vec-transformers.html), and dives into a dataset of wine reviews. This repository demonstrates how to set up Weaviate with your data and get straight to firing up search queries. 

(TODO: Add demo video)

## Prerequisites
(TO DO)

## Setup instructions
1. **Install virtualenv** (if not already installed):
   ```bash
   pip install virtualenv
   ```
2. **Create a Virtual Environment:** Navigate to the directory where you want to create your virtual environment, then run:
   ```bash
   virtualenv <name_of_virtualenv>
   ```

## Usage instructions
1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
2. Install requirements: `pip install -r requirements.txt`
3. Run `python import.py` to import 2500 wines to Weaviate.
4. Navigate to [console.semi.technology](https://console.semi.technology/), connect to `http://localhost:8080`, navigate to the query module, and happy querying!

## Dataset license
This folder contains Wine review data, retrieved from [Kaggle (from WineEnthusiast)](https://www.kaggle.com/zynicide/wine-reviews).

## Notes:
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/semanticsearch-transformers-wines) and the [Hackernoon article: "Semantic Search Queries Return More Informed Results"](https://hackernoon.com/semantic-search-queries-return-more-informed-results-nr5335nw).
